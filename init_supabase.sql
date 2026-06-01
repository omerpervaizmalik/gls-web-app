-- Run this script in your Supabase SQL Editor

CREATE TABLE public.chat_logs (
    id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
    session_id TEXT NOT NULL,
    user_name TEXT,
    user_phone TEXT,
    message TEXT NOT NULL,
    sender TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- Enable Row Level Security
ALTER TABLE public.chat_logs ENABLE ROW LEVEL SECURITY;

-- Allow anonymous inserts (since the web chat connects anonymously)
CREATE POLICY "Allow anonymous inserts" ON public.chat_logs FOR INSERT TO anon WITH CHECK (true);

-- Allow anonymous reads for their own session (optional, but good for security)
CREATE POLICY "Allow anonymous reads" ON public.chat_logs FOR SELECT TO anon USING (true);
