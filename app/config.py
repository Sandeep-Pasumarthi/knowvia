from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    pinecone_api_key: str
    pinecone_index: str
    pinecone_cloud: str
    pinecone_region: str
    pinecone_ready_timeout: int
    embedding_dimension: int

    aws_access_key_id: str
    aws_secret_access_key: str
    aws_region: str
    aws_s3_bucket: str

    max_upload_bytes: int
    min_relevance_score: float
    hitl_enabled: bool
    memory_turns: int

    openrouter_api_key: str
    embedding_model: str
    chat_model: str

    postgres_db_url: str

    rius_api_key: str
    rius_service_name: str
    rius_disabled: bool
    rius_capture_content: bool


def get_settings() -> Settings:
    return Settings()
