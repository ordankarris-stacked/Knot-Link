import React, { useState } from 'react';
import { X, User, Bell, Calendar, Star, MessageSquare, Heart, Share2, MoreHorizontal } from 'lucide-react';

const INITIAL_POSTS = [
  {
    id: 1,
    author: "Weh-nah-noo",
    authorLevel: 15,
    title: "[Post] Did y'all hear? Porcelumex's CEO just got the boot!",
    content: "Heard Porcelumex's CEO Ferox got taken down. Anyone know if this is legit or just rumors?",
    img: "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?q=80&w=800",
    category: "General",
    likes: 42,
    comments: [
      { id: 101, user: "Chop Chop", floor: "1F", text: "Who? Why should we give a Denny about any of this?", avatar: "🦊" },
      { id: 102, user: "Anonymous", floor: "2F", text: "I don't know what's going on, but something must be happening in the Waifei Peninsula. Several TOPS higher-ups have been canceling their events lately, and they're all staying put in Waifei Peninsula — not a single one has left. This whole situation is definitely fishy.", avatar: "👤" },
      { id: 103, user: "Beardy", floor: "3F", text: "Now that he's out of the picture, what about Lucro?", avatar: "🧔" }
    ]
  },
  {
    id: 2,
    author: "MetisIntelligence",
    authorLevel: 42,
    title: "[News] Federal Reserve signals potential rate cut in Q3",
    content: "In a surprising move, the Federal Reserve Chair indicated that inflation targets are nearing the 2% threshold, suggesting a shift in monetary policy.",
    img: "https://images.unsplash.com/photo-1516116216624-53e697fedbea?q=80&w=800",
    category: "General",
    likes: 128,
    comments: []
  }
];

const App = () => {
  const [selectedPost, setSelectedPost] = useState(null);
  const [filter, setFilter] = useState('All');

  return (
    <div className="min-h-screen bg-[#0d0d0d] text-[#e0e0e0] font-sans">
      {/* Top Header */}
      <header className="flex items-center justify-between px-6 py-4 bg-[#121212] border-b border-white/5 sticky top-0 z-50">
        <div className="flex items-center gap-4">
          <div className="bg-[#1a1a1a] rounded-full px-3 py-1 flex items-center gap-2 border border-white/10">
            <div className="w-6 h-6 rounded-full bg-blue-500 flex items-center justify-center text-[10px] font-bold">P</div>
            <div className="text-[10px] font-bold">LV.60</div>
          </div>
        </div>
        <div className="flex gap-4">
           <button className="bg-[#ff4d4d] text-white px-6 py-1.5 rounded-md text-xs font-bold uppercase transition-transform active:scale-95">All</button>
           <button className="bg-[#1a1a1a] text-white/50 px-6 py-1.5 rounded-md text-xs font-bold uppercase hover:text-white">General</button>
           <button className="bg-[#1a1a1a] text-white/50 px-6 py-1.5 rounded-md text-xs font-bold uppercase hover:text-white">Help Info</button>
        </div>
      </header>

      {/* Main Feed */}
      <main className="max-w-4xl mx-auto p-6 space-y-6">
        {INITIAL_POSTS.map(post => (
          <div key={post.id} className="bg-[#151515] rounded-2xl border border-white/5 overflow-hidden transition-all hover:border-white/10">
            <div className="flex flex-col md:flex-row">
              <div className="md:w-1/3 aspect-video md:aspect-square overflow-hidden relative">
                <img src={post.img} className="w-full h-full object-cover opacity-80" alt="" />
                <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" />
              </div>
              <div className="p-6 flex-1 flex flex-col justify-between">
                <div>
                  <div className="flex items-center gap-2 mb-3">
                    <div className="w-4 h-4 rounded-full bg-white/20" />
                    <span className="text-[10px] text-white/40 font-bold uppercase tracking-wider">{post.author}</span>
                  </div>
                  <h2 className="text-lg font-bold leading-snug mb-2">{post.title}</h2>
                  <p className="text-sm text-white/50 line-clamp-2 leading-relaxed">{post.content}</p>
                </div>
                <button 
                  onClick={() => setSelectedPost(post)}
                  className="mt-6 w-full py-2 bg-[#1a1c23] hover:bg-[#252833] border border-white/5 rounded-lg text-xs font-bold tracking-widest text-blue-400 uppercase transition-all"
                >
                  Read Report #{post.id}
                </button>
              </div>
            </div>
          </div>
        ))}
      </main>

      {/* Thread Detail Overlay */}
      {selectedPost && (
        <div className="fixed inset-0 z-[60] flex items-center justify-center p-4">
          <div className="absolute inset-0 bg-black/90 backdrop-blur-md" onClick={() => setSelectedPost(null)} />
          
          <div className="relative w-full max-w-4xl bg-[#111] rounded-3xl border border-white/10 flex flex-col md:flex-row overflow-hidden shadow-2xl h-[80vh]">
            
            {/* Thread Content */}
            <div className="flex-1 overflow-y-auto p-8 border-r border-white/5 custom-scrollbar">
              <div className="flex items-center justify-between mb-8">
                <div className="flex items-center gap-3">
                  <div className="w-12 h-12 rounded-full bg-zinc-800 flex items-center justify-center text-xl border-2 border-white/10">🐷</div>
                  <div>
                    <div className="text-sm font-bold">{selectedPost.author}</div>
                    <div className="bg-zinc-800 px-2 py-0.5 rounded text-[8px] font-black w-fit mt-1 flex items-center gap-1">
                      <Heart size={8} fill="currentColor" /> {selectedPost.authorLevel}
                    </div>
                  </div>
                </div>
                <button onClick={() => setSelectedPost(null)} className="p-2 bg-[#ff3b3b] rounded-xl text-black hover:scale-110 transition-transform">
                  <X size={20} strokeWidth={3} />
                </button>
              </div>

              <div className="space-y-6">
                <div className="rounded-2xl overflow-hidden border border-white/5 aspect-video bg-black">
                   <img src={selectedPost.img} className="w-full h-full object-cover" alt="" />
                </div>
                <h2 className="text-2xl font-black">{selectedPost.title}</h2>
                <p className="text-white/70 leading-relaxed text-sm whitespace-pre-wrap">{selectedPost.content}</p>
              </div>
            </div>

            {/* Comments Sidebar (Matching the image) */}
            <div className="w-full md:w-[350px] bg-[#0c0c0c] flex flex-col">
              <div className="p-4 border-b border-white/5 text-[10px] font-black uppercase tracking-[0.2em] text-white/30">
                Comments & Replies
              </div>
              <div className="flex-1 overflow-y-auto p-4 space-y-4">
                {selectedPost.comments.map(comment => (
                  <div key={comment.id} className="relative group">
                    <div className="flex items-start gap-3">
                      <div className="w-8 h-8 rounded-full bg-[#1a1a1a] flex items-center justify-center text-sm border border-white/5">
                        {comment.avatar}
                      </div>
                      <div className="flex-1">
                        <div className="flex items-center justify-between mb-1">
                          <span className="text-[10px] font-bold text-white/80">{comment.user}</span>
                          <span className="text-[8px] font-black bg-white/5 px-1.5 py-0.5 rounded text-white/40">{comment.floor}</span>
                        </div>
                        <p className="text-[11px] text-white/60 leading-normal">{comment.text}</p>
                      </div>
                    </div>
                    <div className="h-[1px] w-full bg-white/5 mt-4" />
                  </div>
                ))}
              </div>
              <div className="p-4 bg-[#141414] border-t border-white/5">
                <div className="flex items-center gap-2 text-[10px] font-bold text-blue-400 animate-pulse">
                  <div className="w-1.5 h-1.5 rounded-full bg-blue-400" />
                  Live Sync Active
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      <style>{`
        .custom-scrollbar::-webkit-scrollbar { width: 4px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 10px; }
      `}</style>
    </div>
  );
};

export default App;
