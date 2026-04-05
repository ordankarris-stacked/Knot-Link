import React, { useState, useEffect } from 'react';
import { X, ChevronRight, User, Bell, LayoutGrid } from 'lucide-react';

const INITIAL_POSTS = [
  {
    id: 1,
    author: "MetisIntelligence",
    title: "[Post] Vision's shocking scandal exposed — Perlman is going to jail!",
    preview: "Charles Perlman, chief executive of Vision Corp, has been indicted...",
    content: "Charles Perlman, chief executive of Vision Corp, has been indicted on multiple counts of fraud and money laundering following a whistle-blower report. The investigation reveals a massive cover-up involving the new Eridu energy sector.",
    img: "https://images.unsplash.com/photo-1585829365234-781fdb509147?q=80&w=800",
    category: "General",
    replies: [
      { user: "Proxy_X", text: "Finally, justice for the workers.", floor: "1F" },
      { user: "Anon99", text: "I bet he has a backup plan. Vision is too big to fall.", floor: "2F" }
    ]
  },
  {
    id: 2,
    author: "Worrybot",
    title: "A new Hollow on Fourteenth Street!",
    preview: "A Companion Hollow has appeared near the old subway entrance...",
    content: "Observers report a sudden surge in Ether activity near the old subway entrance. Residents are advised to evacuate immediately. Public security has cordoned off the area.",
    img: "https://images.unsplash.com/photo-1478720143022-10dca8de9cc1?q=80&w=800",
    category: "General",
    replies: [
      { user: "Cpt_Safety", text: "Avoid the area at all costs. The corruption levels are peaking.", floor: "1F" }
    ]
  },
  {
    id: 3,
    author: "Friend2Proxy",
    title: "[Info] Proxy Must-Knows: Carrots",
    preview: "Investigators and Proxies often discuss 'Carrots'...",
    content: "Did you know that 'Carrots' aren't just for eating? In the Hollows, they refer to specialized navigational lures. Using them correctly can mean the difference between getting out or getting lost forever.",
    img: "https://images.unsplash.com/photo-1598170845058-32b9d6a5da37?q=80&w=800",
    category: "Help Request Info",
    replies: []
  },
  {
    id: 4,
    author: "gawadaw",
    title: "[Question] How to quickly level up your IK account?",
    preview: "I've been stuck at Level 30 for weeks. Any high-yield commissions?",
    content: "I've been stuck at Level 30 for weeks. Any high-yield commissions I should look out for? I really want to unlock the high-tier tuning materials.",
    img: "https://images.unsplash.com/photo-1550745165-9bc0b252726f?q=80&w=800",
    category: "Help Request Info",
    replies: [
      { user: "IK_Master", text: "Focus on the daily login challenges and priority 'General' posts.", floor: "1F" }
    ]
  }
];

const App = () => {
  const [filter, setFilter] = useState('All');
  const [selectedPost, setSelectedPost] = useState(null);
  const [posts] = useState(INITIAL_POSTS);

  const filteredPosts = posts.filter(post => 
    filter === 'All' || post.category === filter
  );

  return (
    <div className="min-h-screen bg-[#0a0a0a] text-white font-mono selection:bg-yellow-400 selection:text-black">
      {/* Top Header */}
      <header className="flex items-center justify-between px-6 py-4 bg-black/40 backdrop-blur-md sticky top-0 z-40 border-b border-white/5">
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-3 bg-[#1a1a1a] rounded-full px-4 py-2 border border-white/10">
             <div className="w-8 h-8 rounded-full bg-zinc-700 overflow-hidden flex items-center justify-center border border-white/20">
                <User size={20} className="text-zinc-400" />
             </div>
             <div className="pr-2">
                <div className="text-xs text-white/90 font-bold leading-tight tracking-wider uppercase">Anonymous User</div>
                <div className="text-[9px] text-white/30 leading-tight uppercase tracking-widest">Identity Hidden</div>
             </div>
          </div>
        </div>

        <nav className="flex items-center gap-1">
          <button className="flex items-center gap-2 px-6 py-2 rounded-full bg-yellow-400 text-black font-bold text-sm">
            <Bell size={16} /> Notifications
          </button>
          <button className="flex items-center gap-2 px-6 py-2 rounded-full hover:bg-white/5 transition-colors text-sm font-bold">
            <LayoutGrid size={16} /> Intel Board
          </button>
        </nav>
      </header>

      {/* Sub-navigation Filters */}
      <div className="max-w-7xl mx-auto px-6 py-6 flex justify-end gap-2">
        {['All', 'General', 'Help Request Info'].map((cat) => (
          <button
            key={cat}
            onClick={() => setFilter(cat)}
            className={`px-8 py-1 rounded-full text-xs font-bold transition-all ${
              filter === cat
                ? 'bg-yellow-400 text-black'
                : 'bg-[#1a1a1a] text-white/60 hover:bg-[#2a2a2a]'
            }`}
          >
            {cat}
          </button>
        ))}
      </div>

      {/* Grid Feed */}
      <main className="max-w-7xl mx-auto px-6 pb-20">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-5 gap-4">
          {filteredPosts.map((post) => (
            <div
              key={post.id}
              onClick={() => setSelectedPost(post)}
              className="group relative bg-[#151515] rounded-2xl overflow-hidden border-2 border-transparent hover:border-yellow-400 transition-all cursor-pointer flex flex-col h-[380px]"
            >
              {/* Background Image Layer */}
              <div 
                className="h-48 w-full bg-cover bg-center grayscale group-hover:grayscale-0 transition-all duration-500"
                style={{ backgroundImage: `url(${post.img})` }}
              />
              
              {/* Content Layer */}
              <div className="p-4 flex flex-col flex-grow bg-gradient-to-t from-[#111] via-[#151515] to-transparent">
                <div className="flex items-center gap-2 mb-3">
                  <div className="w-6 h-6 rounded-full bg-[#333] flex items-center justify-center text-[10px] border border-white/10">
                    <User size={12} />
                  </div>
                  <span className="text-[10px] font-bold text-white/70 uppercase tracking-tighter truncate">
                    {post.author}
                  </span>
                </div>
                
                <h3 className="text-sm font-bold leading-tight mb-2 group-hover:text-yellow-400 transition-colors line-clamp-3">
                  {post.title}
                </h3>
                
                <p className="text-[11px] text-white/40 line-clamp-2 mt-auto">
                  {post.preview}
                </p>
              </div>
              
              {/* Hover Indicator */}
              <div className="absolute top-2 right-2 opacity-0 group-hover:opacity-100 transition-opacity">
                <div className="bg-yellow-400 text-black p-1 rounded-full">
                  <ChevronRight size={14} />
                </div>
              </div>
            </div>
          ))}
        </div>
      </main>

      {/* Post Modal / Overlay */}
      {selectedPost && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 md:p-8 animate-in fade-in duration-200">
          <div 
            className="absolute inset-0 bg-black/90 backdrop-blur-sm" 
            onClick={() => setSelectedPost(null)}
          />
          
          <div className="relative w-full max-w-4xl bg-[#121212] rounded-3xl border border-white/10 overflow-hidden shadow-2xl flex flex-col md:flex-row h-full max-h-[80vh]">
            
            <div className="md:hidden p-4 border-b border-white/5 flex justify-between items-center bg-[#181818]">
              <span className="text-xs font-bold">{selectedPost.author}</span>
              <button onClick={() => setSelectedPost(null)} className="p-1 hover:bg-white/10 rounded-full">
                <X size={20} />
              </button>
            </div>

            <div className="flex-1 overflow-y-auto p-6 md:p-10 custom-scrollbar">
              <div className="relative aspect-video rounded-xl overflow-hidden mb-8 border border-white/10">
                 <img src={selectedPost.img} className="w-full h-full object-cover" alt="" />
                 <div className="absolute top-4 left-4 bg-blue-500 text-white text-[10px] font-black px-3 py-1 rounded-full uppercase italic shadow-lg">
                   {selectedPost.category === 'General' ? 'Proxy Commissions' : 'Information'}
                 </div>
              </div>

              <div className="space-y-4">
                <div className="flex items-center gap-3 mb-2">
                  <div className="w-10 h-10 rounded-full bg-[#222] border border-white/10 flex items-center justify-center">
                    <User size={20} className="text-white/40" />
                  </div>
                  <div>
                    <div className="text-sm font-bold tracking-tight">{selectedPost.author}</div>
                    <div className="text-[10px] text-white/30">ID: {selectedPost.id * 1492}</div>
                  </div>
                </div>

                <h1 className="text-2xl font-black leading-tight text-white italic tracking-tighter">
                  {selectedPost.title}
                </h1>
                
                <p className="text-white/70 leading-relaxed text-sm border-l-2 border-yellow-400 pl-4 py-1">
                  {selectedPost.content}
                </p>
              </div>
            </div>

            <div className="w-full md:w-[350px] bg-[#0d0d0d] border-l border-white/5 flex flex-col">
              <div className="p-4 border-b border-white/5 hidden md:flex justify-between items-center">
                <span className="text-xs font-bold text-white/40">REPLIES ({selectedPost.replies.length})</span>
                <button 
                  onClick={() => setSelectedPost(null)}
                  className="bg-red-500 hover:bg-red-600 p-1 rounded-lg transition-colors"
                >
                  <X size={18} />
                </button>
              </div>

              <div className="flex-grow overflow-y-auto p-4 space-y-6 custom-scrollbar">
                {selectedPost.replies.length > 0 ? (
                  selectedPost.replies.map((reply, i) => (
                    <div key={i} className="group animate-in slide-in-from-right-4 duration-300" style={{ animationDelay: `${i * 100}ms` }}>
                      <div className="flex items-center justify-between mb-2">
                        <div className="flex items-center gap-2">
                          <div className="w-5 h-5 rounded-full bg-white/10 flex items-center justify-center overflow-hidden">
                            <User size={10} />
                          </div>
                          <span className="text-[11px] font-bold text-white/80">{reply.user}</span>
                        </div>
                        <span className="text-[10px] text-white/20 bg-white/5 px-1.5 py-0.5 rounded">{reply.floor}</span>
                      </div>
                      <p className="text-xs text-white/50 leading-normal pl-7">
                        {reply.text}
                      </p>
                    </div>
                  ))
                ) : (
                  <div className="h-full flex items-center justify-center opacity-20 italic text-sm">
                    No one has replied yet...
                  </div>
                )}
              </div>

              <div className="p-4 bg-[#151515] border-t border-white/5">
                <div className="flex items-center gap-2 bg-black/40 rounded-xl p-2 border border-white/5">
                  <input 
                    type="text" 
                    placeholder="Type your reply..." 
                    className="flex-grow bg-transparent border-none focus:outline-none text-xs p-1"
                  />
                  <button className="bg-yellow-400 text-black text-[10px] font-bold px-3 py-1 rounded-lg">
                    SEND
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      <style dangerouslySetInnerHTML={{ __html: `
        .custom-scrollbar::-webkit-scrollbar {
          width: 4px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
          background: transparent;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
          background: #333;
          border-radius: 10px;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {
          background: #444;
        }
      `}} />
    </div>
  );
};

export default App;
