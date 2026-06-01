-- Run this in your Supabase SQL Editor to create the Judgments database for your clients

CREATE TABLE public.judgments (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    title TEXT NOT NULL,
    pdf_url TEXT NOT NULL UNIQUE,
    tagline TEXT,
    upload_date DATE,
    court TEXT DEFAULT 'Lahore High Court',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- Enable Row Level Security (RLS)
ALTER TABLE public.judgments ENABLE ROW LEVEL SECURITY;

-- Allow anonymous reads so your clients can search and download cases
CREATE POLICY "Allow public read access to judgments" ON public.judgments FOR SELECT TO anon USING (true);

-- Allow anonymous inserts (only temporarily or restrict via service role later if needed, but for the GitHub Action using ANON key it needs insert)
CREATE POLICY "Allow public insert to judgments" ON public.judgments FOR INSERT TO anon WITH CHECK (true);
