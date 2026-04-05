import React, { useState, useEffect } from 'react';
import { X, ChevronRight, User, Bell, LayoutGrid, Flame, TrendingUp, MessageSquare, ShieldAlert } from 'lucide-react';

const TRENDING_TOPICS = [
  { id: 1, title: "Trump issues warning to Iran", sub: "Trump Vows To Strike Civilian Infrastructure...", tag: "r/politics", img: "https://images.unsplash.com/photo-1580130281216-33b47f4528e2?q=80&w=800" },
  { id: 2, title: "US rescues missing pilot", sub: "U.S. forces rescue second crew member...", tag: "r/worldnews", img: "https://images.unsplash.com/photo-1508614589041-895b88991e3e?q=80&w=800" },
  { id: 3, title: "New Artemis II photos", sub: "New image from NASA: For the first tim...", tag: "r/spaceporn", img: "https://images.unsplash.com/photo-1446776811953-b23d57bd21aa?q=80&w=800" },
  { id: 4, title: "Pepsi pulls out of Wi...", sub: "Pepsi Cancels Sponsorship c...", tag: "r/Music", img: "https://images.unsplash.com/photo-1551028719-00167b16eac5?q=80&w=800" }
];

const INITIAL_POSTS = [
  {
    id: 101,
    author: "Obsidian Blade",
    likes: 3960,
    title: "[Commission] Obsidian: Strategic Eradication",
    preview: "Hollow activity has drastically diminished. Maximum alert level has now been temporarily lifted!",
    content: "I am the captain of a mercenary troupe hired by Obsidian Division. Hollow activity has crossed the warning threshold, and Obsidian Division have adopted the most extreme suppression program: Indiscriminate extermination of all living things inside the Hollow...",
    img: "https://images.unsplash.com/photo-1614728263952-84ea206f99b6?q=80&w=800",
    category: "General",
    replies: [
      { user: "Kitty_Freak", text: "That's terrifying... I'm keeping well away from the Hollows for now!", floor: "1F" },
      { user: "Fantastical_Balut", text: "There's no room for argument with Obsidian Division... *sigh*", floor: "2F" },
      { user: "Doomed_Once_Daily", text: "Doesn't really sound as though OP has any choice...", floor: "3F" }
    ]
  },
  {
    id: 102,
    author: "Weh-nah-noo",
    likes: 15,
    title: "[Post] Did y'all hear? Porcelumex's CEO just got the boot!",
    preview: "Heard Porcelumex's CEO Ferox got taken down. Anyone know if this is legit?",
    content: "Heard Porcelumex's CEO Ferox got taken down. Anyone know if this is legit or just rumors? Something must be happening in the Waifei Peninsula. Several TOPS higher-ups have been canceling events lately.",
    img: "https://images.unsplash.com/photo-1551836022-d5d88e9218df?q=80&w=800",
    category: "General",
    replies: [
      { user: "Chop Chop", text: "Who? Why should we give a Denny about any of this?", floor: "1F" },
      { user: "Anonymous", text: "The whole situation is definitely fishy. Not a single one has left the peninsula.", floor: "2F" }
    ]
  },
  {
    id: 103,
    author: "Reuters_Global",
    likes: 820,
    title: "[News] Federal Reserve signals potential rate cut in Q3",
    preview: "In a surprising move, the Federal Reserve Chair indicated that inflation targets are nearing...",
    content: "In a surprising move, the Federal Reserve Chair indicated that inflation targets are nearing the 2% threshold, suggesting a shift in monetary policy to support labor market stability.",
    img: "https://images.unsplash.com/photo-1611974714158-f89644d67c1e?q=80&w=800",
    category: "Help Info",
    replies: []
  }
];

const App = () => {
  const [filter, setFilter] = useState('All');
  const [selectedPost, setSelectedPost] = useState(null);

  const filteredPosts = INITIAL_POSTS.filter(post => 
    filter === 'All' || post.category === filter
  );

  return (
    <div className="min-h-screen bg-[#080808] text-zinc-100 font-sans selection:bg-yellow-400 selection:text-black">
      {/* Top Header */}
      <header className="flex items-center justify-between px-8 py-4 bg-[#0a0a0a]/80 backdrop-blur-xl sticky top-0 z-50 border-b border-white/5">
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-3 bg-[#1a1a1a] rounded-xl px-4 py-2 border border-white/10">
             <div className="w-9 h-9 rounded-full bg-zinc-800 flex items-center justify-center border border-white/10 shadow-inner">
                <User size={20} className="text-zinc-500" />
             </div>
             <div>
                <div className="text-sm font-black tracking-tight text-white uppercase italic">Anonymous User</div>
                <div className="flex items-center gap-1.5">
                  <div className="w-1.5 h-1.5 rounded-full bg-green-500 animate-pulse"></div>
                  <div className="text-[10px] text-zinc-500 font-bold uppercase tracking-widest">Status: Hidden</div>
                </div>
             </div>
          </div>
        </div>

        <nav className="flex items-center gap-4">
          <button className="flex items-center gap-2 px-5 py-2 rounded-xl bg-zinc-900 hover:bg-zinc-800 transition-all border border-white/5 font-bold text-xs uppercase tracking-widest">
            <Bell size={14} className="text-yellow-400" /> Notifications
          </button>
          <button className="flex items-center gap-2 px-5 py-2 rounded-xl bg-white text-black font-black text-xs uppercase tracking-widest hover:bg-yellow-400 transition-colors">
            <LayoutGrid size={14} /> Intel Board
          </button>
        </nav>
      </header>

      <main className="max-w-[1600px] mx-auto px-8 py-8">
        {/* Trending Section (from your first image) */}
        <section className="mb-12">
          <div className="flex items-center gap-2 mb-6 ml-2">
            <Flame size={20} className="text-orange-500" />
            <h2 className="text-lg font-black italic uppercase tracking-tighter">Hot Intel</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
            {TRENDING_TOPICS.map((topic) => (
              <div 
                key={topic.id} 
                className="group relative h-48 rounded-2xl overflow-hidden cursor-pointer border border-white/5 hover:border-yellow-400/50 transition-all shadow-2xl"
              >
                <img src={topic.img} className="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-110" alt="" />
                <div className="absolute inset-0 bg-gradient-to-t from-black via-black/40 to-transparent" />
                <div className="absolute bottom-0 left-0 p-4 w-full">
                  <h3 className="font-bold text-sm leading-tight mb-1 group-hover:text-yellow-400 transition-colors">{topic.title}</h3>
                  <p className="text-[10px] text-zinc-400 line-clamp-1 mb-2">{topic.sub}</p>
                  <div className="flex items-center gap-1.5 opacity-80">
                    <div className="w-4 h-4 rounded-full bg-white/20 flex items-center justify-center">
                      <TrendingUp size={10} />
                    </div>
                    <span className="text-[10px] font-bold text-white/60">{topic.tag}</span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Filter Navigation */}
        <div className="flex justify-center gap-3 mb-8">
          {['All', 'General', 'Help Info'].map((cat) => (
            <button
              key={cat}
              onClick={() => setFilter(cat)}
              className={`px-12 py-2 rounded-lg text-xs font-black transition-all italic tracking-widest border ${
                filter === cat
                  ? 'bg-red-500 border-red-400 text-white shadow-[0_0_20px_rgba(239,68,68,0.3)]'
                  : 'bg-[#151515] border-white/5 text-zinc-500 hover:text-white hover:bg-zinc-800'
              }`}
            >
              {cat.toUpperCase()}
            </button>
          ))}
        </div>

        {/* Post Grid (Obsidian style) */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredPosts.map((post) => (
            <div
              key={post.id}
              onClick={() => setSelectedPost(post)}
              className="bg-[#121212] rounded-3xl border border-white/5 hover:border-yellow-400/30 transition-all p-5 cursor-pointer group shadow-xl"
            >
              <div className="flex items-center justify-between mb-4">
                <div className="flex items-center gap-2">
                  <div className="w-8 h-8 rounded-lg bg-zinc-800 flex items-center justify-center border border-white/5">
                    <User size={16} className="text-zinc-500" />
                  </div>
                  <div>
                    <div className="text-xs font-bold text-white/90">{post.author}</div>
                    <div className="text-[10px] text-zinc-500 italic">#{post.likes} Merit</div>
                  </div>
                </div>
                <div className="text-[10px] bg-blue-500/10 text-blue-400 px-2 py-0.5 rounded border border-blue-500/20 font-bold">
                  {post.category.toUpperCase()}
                </div>
              </div>

              <div className="aspect-[16/9] rounded-2xl overflow-hidden mb-4 relative">
                <img src={post.img} className="w-full h-full object-cover grayscale-[0.5] group-hover:grayscale-0 transition-all duration-500" alt="" />
                <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-end p-4">
                  <div className="bg-yellow-400 text-black text-[10px] font-black px-3 py-1 rounded-full italic">READ REPORT</div>
                </div>
              </div>

              <h3 className="font-bold text-base leading-snug mb-2 group-hover:text-yellow-400 transition-colors line-clamp-2 italic">
                {post.title}
              </h3>
              <p className="text-xs text-zinc-500 line-clamp-2 leading-relaxed">
                {post.preview}
              </p>
            </div>
          ))}
        </div>
      </main>

      {/* Detail Modal */}
      {selectedPost && (
        <div className="fixed inset-0 z-[100] flex items-center justify-center p-6 animate-in zoom-in-95 duration-200">
          <div className="absolute inset-0 bg-black/95 backdrop-blur-md" onClick={() => setSelectedPost(null)} />
          
          <div className="relative w-full max-w-5xl bg-[#111] rounded-[2rem] border-2 border-white/5 overflow-hidden flex flex-col md:flex-row h-[85vh] shadow-[0_0_100px_rgba(0,0,0,1)]">
            
            {/* Close Button Overlay */}
            <button 
              onClick={() => setSelectedPost(null)}
              className="absolute top-6 right-6 z-10 bg-red-500 hover:bg-red-600 p-2 rounded-xl text-white transition-all hover:scale-110 shadow-lg"
            >
              <X size={24} strokeWidth={3} />
            </button>

            {/* Content Area */}
            <div className="flex-1 overflow-y-auto p-8 md:p-12 scroll-smooth custom-scrollbar">
              <div className="flex items-center gap-4 mb-8">
                <div className="w-14 h-14 rounded-2xl bg-zinc-800 border border-white/10 flex items-center justify-center">
                  <User size={32} className="text-zinc-500" />
                </div>
                <div>
                  <h4 className="text-xl font-black italic uppercase tracking-tight">{selectedPost.author}</h4>
                  <div className="text-xs text-zinc-500 font-mono tracking-widest uppercase">ID: NODE_{selectedPost.id * 142}</div>
                </div>
              </div>

              <div className="rounded-3xl overflow-hidden mb-8 border border-white/5 shadow-2xl">
                <img src={selectedPost.img} className="w-full object-cover max-h-[400px]" alt="" />
              </div>

              <div className="bg-yellow-400/5 border-l-4 border-yellow-400 p-6 rounded-r-2xl mb-8">
                <h2 className="text-2xl font-black italic mb-4 leading-tight">
                  {selectedPost.title}
                </h2>
                <div className="text-zinc-300 leading-relaxed text-sm font-medium space-y-4">
                  {selectedPost.content}
                </div>
              </div>
            </div>

            {/* Sidebar Replies (Obsidian style) */}
            <div className="w-full md:w-[400px] bg-[#0c0c0c] border-l border-white/5 flex flex-col">
              <div className="p-6 border-b border-white/5 flex items-center justify-between bg-zinc-900/30">
                <div className="flex items-center gap-2">
                  <MessageSquare size={16} className="text-yellow-400" />
                  <span className="text-xs font-black uppercase tracking-widest text-zinc-400 italic">Discussion</span>
                </div>
                <div className="text-[10px] font-bold bg-zinc-800 px-2 py-1 rounded text-zinc-500">
                  {selectedPost.replies.length} REPLIES
                </div>
              </div>

              <div className="flex-grow overflow-y-auto p-6 space-y-8 custom-scrollbar">
                {selectedPost.replies.map((reply, i) => (
                  <div key={i} className="animate-in slide-in-from-bottom-4 duration-500" style={{ animationDelay: `${i * 150}ms` }}>
                    <div className="flex items-center justify-between mb-2">
                      <div className="flex items-center gap-2">
                        <div className="w-6 h-6 rounded bg-zinc-800 flex items-center justify-center border border-white/5">
                          <User size={12} />
                        </div>
                        <span className="text-[11px] font-black text-zinc-300 italic">{reply.user}</span>
                      </div>
                      <span className="text-[9px] font-mono text-zinc-600 bg-white/5 px-2 py-0.5 rounded uppercase tracking-widest">{reply.floor}</span>
                    </div>
                    <p className="text-xs text-zinc-500 leading-normal pl-8 border-l border-white/5 ml-3">
                      {reply.text}
                    </p>
                  </div>
                ))}
              </div>

              <div className="p-6 bg-[#0a0a0a] border-t border-white/5">
                <div className="relative group">
                  <input 
                    type="text" 
                    placeholder="Contribute to thread..." 
                    className="w-full bg-zinc-900 border-2 border-white/5 rounded-xl py-3 px-4 pr-12 text-xs focus:outline-none focus:border-yellow-400/50 transition-all italic font-medium"
                  />
                  <button className="absolute right-2 top-1.5 bottom-1.5 px-4 bg-yellow-400 text-black text-[10px] font-black rounded-lg hover:bg-white transition-colors">
                    POST
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Global CSS for scrollbars */}
      <style dangerouslySetInnerHTML={{ __html: `
        .custom-scrollbar::-webkit-scrollbar { width: 5px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: transparent; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #222; border-radius: 10px; }
        .custom-scrollbar::-webkit-scrollbar-thumb:hover { background: #333; }
      `}} />
    </div>
  );
};

export default App;
