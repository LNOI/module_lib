from pydantic_settings import BaseSettings


class Config(BaseSettings):
    MINIO_ENDPOINT: str | None = "localhost:9000"
    MINIO_ACCESS_KEY: str | None = "rsueM445wIe6sIaSvDEy"
    MINIO_SECRET_KEY: str | None = None
    MINIO_SECURE: bool = False
    MINIO_BUCKET_NAME: str | None = "english"


config = Config()
