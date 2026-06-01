"use client";

import { useState } from 'react';
import JoditWrapper from './JoditWrapper';

export default function LegalAssistant() {
  const [documentType, setDocumentType] = useState('Agreement of Collaboration');
  const [prompt, setPrompt] = useState('I need a standard agreement of collaboration between John Doe and Jane Smith starting on October 1st, 2026.');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleDraft = async () => {
    setLoading(true);
    try {
      const res = await fetch('/api/draft', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          documentType,
          prompt
        })
      });
      const data = await res.json();
      
      if (data.error) {
        setOutput('Error: ' + data.error);
      } else {
        setOutput(data.result);
      }
    } catch (err) {
      setOutput('Error: Server failure. Please check your network or terminal for details.');
    }
    setLoading(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-[#0f172a] via-[#1e293b] to-[#0f172a] p-4 md:p-8 font-sans text-slate-200">
      
      {/* Header / Logo Area */}
      <div className="max-w-6xl mx-auto mb-8 flex items-center gap-4">
        <div className="w-12 h-12 rounded-lg bg-gradient-to-tr from-amber-500 to-yellow-300 flex items-center justify-center shadow-lg shadow-amber-500/20">
            {/* User can replace this SVG with their actual <img> logo */}
            <svg className="w-8 h-8 text-slate-900" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/></svg>
        </div>
        <div>
            <h1 className="text-3xl font-bold tracking-tight text-white drop-shadow-md">GLS <span className="text-amber-400 font-light">AI ASSISTANT</span></h1>
            <p className="text-sm text-slate-400">Powered by Get Legal Solution Intelligence</p>
        </div>
      </div>
      
      <div className="max-w-6xl mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        {/* Left Panel: Inputs */}
        <div className="lg:col-span-5 space-y-6">
          <div className="bg-white/5 backdrop-blur-xl border border-white/10 p-6 rounded-2xl shadow-2xl">
            <h2 className="text-xl font-semibold mb-6 text-white border-b border-white/10 pb-4 flex items-center gap-2">
                <svg className="w-5 h-5 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" /></svg>
                Drafting Parameters
            </h2>
            
            <div className="space-y-5">
              <div>
                <label className="block text-sm font-medium mb-2 text-slate-300">Select Template Context</label>
                <select 
                  value={documentType} 
                  onChange={e => setDocumentType(e.target.value)}
                  className="w-full bg-slate-900/50 border border-slate-700 rounded-xl p-3 text-white focus:ring-2 focus:ring-amber-500 outline-none transition-all"
                >
                  <option value="Agreement of Collaboration">Agreement of Collaboration (English)</option>
                  <option value="Authorization Letter For Vehicle use">Vehicle Authorization Letter (English)</option>
                  <option value="Rent Deed Urdu">Rent Deed (Urdu)</option>
                  <option value="POST AREEST BAIL">Post Arrest Bail (English)</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-medium mb-2 text-slate-300">Prompt / Requirements</label>
                <textarea 
                  value={prompt}
                  onChange={e => setPrompt(e.target.value)}
                  className="w-full bg-slate-900/50 border border-slate-700 rounded-xl p-3 h-48 font-mono text-sm text-amber-200 focus:ring-2 focus:ring-amber-500 outline-none transition-all scrollbar-thin scrollbar-thumb-slate-700"
                  placeholder="Type all your requirements here, like Gemini..."
                />
              </div>

              <div className="pt-4">
                 <button 
                   onClick={() => handleDraft()} 
                   disabled={loading}
                   className="w-full relative group overflow-hidden rounded-xl p-[1px]"
                 >
                   <span className="absolute inset-0 bg-gradient-to-r from-amber-500 to-yellow-300 rounded-xl opacity-70 group-hover:opacity-100 transition-opacity duration-300"></span>
                   <div className="relative bg-slate-900 px-4 py-4 rounded-xl flex items-center justify-center gap-2 group-hover:bg-opacity-0 transition-all duration-300">
                      {loading ? (
                          <span className="text-white font-bold flex items-center gap-2">
                            <svg className="animate-spin h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle><path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
                            Drafting...
                          </span>
                      ) : (
                          <span className="text-white font-bold text-lg">Generate Document</span>
                      )}
                   </div>
                 </button>
              </div>

            </div>
          </div>
        </div>

        {/* Right Panel: Output Viewer */}
        <div className="lg:col-span-7">
          <div className="bg-[#f8f9fa] h-full min-h-[600px] p-8 rounded-2xl shadow-2xl border border-slate-300 flex flex-col relative overflow-hidden">
            {/* Watermark */}
            <div className="absolute inset-0 flex items-center justify-center opacity-[0.03] pointer-events-none">
                <span className="text-9xl font-black text-slate-900 rotate-[-45deg] whitespace-nowrap">GLS LEGAL</span>
            </div>

            <div className="flex items-center justify-between mb-6 border-b border-slate-300 pb-4 relative z-10">
                <h2 className="text-xl font-bold text-slate-800 flex items-center gap-2">
                    <svg className="w-5 h-5 text-slate-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
                    Generated Document
                </h2>
                <div className="flex gap-2">
                    <div className="w-3 h-3 rounded-full bg-red-400"></div>
                    <div className="w-3 h-3 rounded-full bg-amber-400"></div>
                    <div className="w-3 h-3 rounded-full bg-emerald-400"></div>
                </div>
            </div>

            <div className="flex-1 relative z-10 w-full h-full pb-4">
                <JoditWrapper content={output} setContent={setOutput} />
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}
