"use client";

import dynamic from 'next/dynamic';
import { useRef, useMemo } from 'react';

// Dynamically import Jodit Editor to prevent "document is not defined" SSR errors
const JoditEditor = dynamic(() => import('jodit-react'), { ssr: false });

export default function JoditWrapper({ content, setContent }: { content: string, setContent: (val: string) => void }) {
    const editor = useRef(null);

    const config = useMemo(() => ({
        readonly: false,
        placeholder: 'Generated legal draft will appear here. You can fully format it like MS Word...',
        height: 800,
        toolbarSticky: false,
        buttons: [
            'source', '|',
            'bold', 'italic', 'underline', 'strikethrough', '|',
            'superscript', 'subscript', '|',
            'ul', 'ol', '|',
            'outdent', 'indent', '|',
            'font', 'fontsize', 'brush', 'paragraph', '|',
            'image', 'table', 'link', '|',
            'align', 'undo', 'redo', '|',
            'hr', 'eraser', 'copyformat', '|',
            'symbol', 'fullsize', 'print'
        ]
    }), []);

    return (
        <div className="bg-white text-black p-4 rounded shadow">
            <JoditEditor
                ref={editor}
                value={content}
                config={config}
                onBlur={newContent => setContent(newContent)}
                onChange={() => {}}
            />
        </div>
    );
}
