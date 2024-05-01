# Python の公式イメージをベースとして使用
FROM python:3.12-slim AS base

# 作業ディレクトリを設定
WORKDIR /usr/local/environment-data

# requirements.txt をコンテナ内の作業ディレクトリにコピー
COPY requirements.txt ./

# 必要な Python パッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

 
FROM base AS develop

# install gc\oogle cloud cli
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates gnupg curl git && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    apt-get update && apt-get -y install google-cloud-cli
