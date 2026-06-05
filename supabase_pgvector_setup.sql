-- 1. Enable the pgvector extension to handle AI embeddings
create extension if not exists vector;

-- 2. Create the document_chunks table to store the actual text and AI vectors
create table if not exists document_chunks (
  id bigserial primary key,
  judgment_id bigint references judgments(id) on delete cascade,
  content text not null,
  embedding vector(768) not null
);

-- 3. Create an index for faster similarity searches
create index on document_chunks using ivfflat (embedding vector_cosine_ops)
with (lists = 100);

-- 4. Create the search function for the AI RAG to use
create or replace function match_document_chunks(
  query_embedding vector(768),
  match_threshold float,
  match_count int
)
returns table (
  id bigint,
  judgment_id bigint,
  content text,
  similarity float,
  title text,
  pdf_url text
)
language sql stable
as $$
  select
    document_chunks.id,
    document_chunks.judgment_id,
    document_chunks.content,
    1 - (document_chunks.embedding <=> query_embedding) as similarity,
    judgments.title,
    judgments.pdf_url
  from document_chunks
  join judgments on judgments.id = document_chunks.judgment_id
  where 1 - (document_chunks.embedding <=> query_embedding) > match_threshold
  order by similarity desc
  limit match_count;
$$;
