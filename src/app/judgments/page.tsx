"use client";

import { useState, useEffect } from "react";
import { createClient } from "@supabase/supabase-js";

// Initialize Supabase Client
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!;
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!;
const supabase = createClient(supabaseUrl, supabaseAnonKey);

export default function JudgmentsPage() {
  const [query, setQuery] = useState("");
  const [judgments, setJudgments] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  // Initial load
  useEffect(() => {
    fetchLatestJudgments();
  }, []);

  const fetchLatestJudgments = async () => {
    setLoading(true);
    const { data, error } = await supabase
      .from("judgments")
      .select("*")
      .order("upload_date", { ascending: false })
      .limit(20);

    if (error) {
      console.error("Error fetching judgments:", error);
    } else {
      setJudgments(data || []);
    }
    setLoading(false);
  };

  const handleSearch = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query) return fetchLatestJudgments();

    setLoading(true);
    // Simple ILIKE search across title and tagline
    const { data, error } = await supabase
      .from("judgments")
      .select("*")
      .or(`title.ilike.%${query}%,tagline.ilike.%${query}%`)
      .order("upload_date", { ascending: false })
      .limit(50);

    if (error) {
      console.error("Error searching judgments:", error);
    } else {
      setJudgments(data || []);
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <div className="max-w-5xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-extrabold text-gray-900 sm:text-5xl">
            Case Law Database
          </h1>
          <p className="mt-4 text-xl text-gray-500">
            Search our comprehensive database of latest reported judgments from the Lahore High Court.
          </p>
        </div>

        {/* Search Bar */}
        <div className="bg-white p-6 rounded-lg shadow-md mb-8">
          <form onSubmit={handleSearch} className="flex gap-4">
            <input
              type="text"
              className="flex-1 p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500"
              placeholder="Search by case title, citation, or keywords..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
            />
            <button
              type="submit"
              className="px-6 py-3 bg-indigo-600 text-white font-medium rounded-md hover:bg-indigo-700 transition-colors"
            >
              Search
            </button>
          </form>
        </div>

        {/* Results */}
        {loading ? (
          <div className="text-center py-12">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-indigo-600 mx-auto"></div>
            <p className="mt-4 text-gray-500">Searching database...</p>
          </div>
        ) : (
          <div className="space-y-6">
            {judgments.map((judgment) => (
              <div key={judgment.id} className="bg-white p-6 rounded-lg shadow-sm border border-gray-200 transition-shadow hover:shadow-md">
                <div className="flex justify-between items-start">
                  <div className="pr-8">
                    <h2 className="text-xl font-bold text-gray-900 mb-2">
                      {judgment.title}
                    </h2>
                    {judgment.tagline && (
                      <p className="text-gray-600 mb-4 line-clamp-3">
                        {judgment.tagline}
                      </p>
                    )}
                    <div className="flex gap-4 text-sm text-gray-500">
                      <span>🏛️ {judgment.court}</span>
                      <span>📅 Uploaded: {judgment.upload_date}</span>
                    </div>
                  </div>
                  <a
                    href={judgment.pdf_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex-shrink-0 flex items-center justify-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-indigo-700 bg-indigo-100 hover:bg-indigo-200"
                  >
                    Download PDF
                  </a>
                </div>
              </div>
            ))}
            
            {judgments.length === 0 && (
              <div className="text-center py-12 bg-white rounded-lg border border-gray-200">
                <p className="text-gray-500 text-lg">No judgments found matching "{query}".</p>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
