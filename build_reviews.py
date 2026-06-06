import os

# Complete, cleaned dataset matching your full product file data
products = [
    {"code": "LFM001", "name": "Snitch Twilight Blue Shirt", "yt": "https://youtube.com/shorts/cVrFyxfkVsA", "affiliate": "https://ajiio.in/Pkz8ur6", "store": "AJIO", "category": "Shirt"},
    {"code": "LFM002", "name": "British Club Checked Slim Fit Shirt", "yt": "https://youtube.com/shorts/Ef-KsWv6m9k", "affiliate": "https://ajiio.in/bqRMXnK", "store": "AJIO", "category": "Shirt"},
    {"code": "LFM003", "name": "Bene Kleed Beige Boot Cut Jeans", "yt": "https://youtube.com/shorts/QxsK3lHyLmg", "affiliate": "https://ajiio.in/m6PDE1y", "store": "AJIO", "category": "Jeans"},
    {"code": "LFM004", "name": "Campus Sutra ripped shirt", "yt": "https://youtube.com/shorts/PHnAnxCAoNA", "affiliate": "https://ajiio.in/g7LvJuF", "store": "AJIO", "category": "Shirt"},
    {"code": "LFM005", "name": "The Bear House Men Checked Slim Fit Shirt", "yt": "https://youtube.com/shorts/9Wq5vP-WVds", "affiliate": "https://ajiio.in/dd40lF7", "store": "AJIO", "category": "Shirt"},
    {"code": "LFM006", "name": "BENE KLEED Men Mid Rise Jeans", "yt": "https://youtube.com/shorts/Ofq2dD6wUA", "affiliate": "https://ajiio.in/m6PDE1y", "store": "AJIO", "category": "Jeans"},
    {"code": "LFM007", "name": "TEAMSPIRIT Men Regular Fit Polo T-Shirt", "yt": "https://youtube.com/shorts/UQFditSw85M", "affiliate": "https://ajiio.in/Th0DPJ1", "store": "AJIO", "category": "T-Shirt"},
    {"code": "LFM008", "name": "Sparx Men Textured Thong Flip-Flops", "yt": "https://youtube.com/shorts/euW2tlpedw4", "affiliate": "https://myntr.it/6FVQ6kG", "store": "Myntra", "category": "Footwear"},
    {"code": "LFM009", "name": "KOTTY Men Man Regular Fit Jeans", "yt": "https://youtube.com/shorts/1mncOSGu96l", "affiliate": "https://ajiio.in/6vl5L4D", "store": "AJIO", "category": "Jeans"},
    {"code": "LFM010", "name": "TEAMSPIRIT Men Straight Fit Track Pants", "yt": "https://youtube.com/shorts/vhPRujBfvGc", "affiliate": "https://ajiio.in/OfxykxE", "store": "AJIO", "category": "Pants"},
    {"code": "LFM011", "name": "YOUSTA Men Low-Top Lace-Up Sneakers", "yt": "https://youtube.com/shorts/FeXUB8eKI-0", "affiliate": "https://ajiio.in/c1YyGIC", "store": "AJIO", "category": "Footwear"},
    {"code": "LFM012", "name": "HERE&NOW Men Opaque Casual Shirt", "yt": "https://youtube.com/shorts/BQ5-FVvdtM", "affiliate": "https://myntr.it/P4K2tZm", "store": "Myntra", "category": "Shirt"},
    {"code": "LFM013", "name": "PERFORMAX Ultra Lightweight Running T-Shirt", "yt": "https://youtube.com/shorts/eXTPg-KBbts", "affiliate": "https://ajiio.in/QHdsiN7", "store": "AJIO", "category": "T-Shirt"},
    {"code": "LFM014", "name": "HRX by Hrithik Roshan Mesh Running Shoes", "yt": "https://youtube.com/shorts/D3SjwXRRF2Y", "affiliate": "https://myntr.it/VbA6Y03", "store": "Myntra", "category": "Footwear"},
    {"code": "LFM015", "name": "LEE COOPER Men Regular Fit Shirt", "yt": "https://youtube.com/shorts/XOUFJXSbTFI", "affiliate": "https://ajiio.in/1BXhxvw", "store": "AJIO", "category": "Shirt"},
    {"code": "LFM016", "name": "ARROW Men Tapered Fit Trousers", "yt": "https://youtube.com/shorts/X54S1ZKNKNo", "affiliate": "https://ajiio.in/hm8nlwt", "store": "AJIO", "category": "Trousers"},
    {"code": "LFM017", "name": "PERFORMAX Men Regular Fit Crew-Neck T-Shirt", "yt": "https://youtube.com/shorts/eAM59L6kUCk", "affiliate": "https://ajiio.in/7xY81kA", "store": "AJIO", "category": "T-Shirt"},
    {"code": "LFM018", "name": "PUMA Men's Slim Fit Polo T-Shirt", "yt": "https://youtube.com/shorts/WFNFkdkPUmk", "affiliate": "https://ajiio.in/NelSc1y", "store": "AJIO", "category": "T-Shirt"},
    {"code": "LFM019", "name": "KAPPA Regular Fit Polo T-Shirt", "yt": "https://youtube.com/shorts/csFz2Ji2TW4", "affiliate": "https://ajiio.in/8em6eJH", "store": "AJIO", "category": "T-Shirt"},
    {"code": "LFM020", "name": "PERFORMAX Men Dual-Strap Sandals", "yt": "https://youtube.com/shorts/BPajO78EeL4", "affiliate": "https://ajiio.in/A6cLnxR", "store": "AJIO", "category": "Footwear"},
    {"code": "LFM021", "name": "SNITCH Men Lightly-Washed Straight Fit Jeans", "yt": "https://youtube.com/shorts/QvMXBtKmcno", "affiliate": "https://ajiio.in/s10UunX", "store": "AJIO", "category": "Jeans"},
    {"code": "LFM022", "name": "PERFORMAX Men Regular Fit Shorts", "yt": "https://youtube.com/shorts/OTHVp59BTs", "affiliate": "https://ajiio.in/Ouusp9r", "store": "AJIO", "category": "Shorts"},
    {"code": "LFM023", "name": "Dockstreet Men Striped Black Track Pants", "yt": "https://youtube.com/shorts/NUBxZdJGsTM", "affiliate": "https://fktr.in/OuGo7te", "store": "Flipkart", "category": "Pants"}
]

# Locked in with your precise Google Tracking Key
GA_TRACKING_ID = "G-F3YXR4NZHB"

review_template = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id={ga_id}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{ga_id}');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="referrer" content="strict-origin-when-cross-origin">
    <title>{name} | LESSFORMORE</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ serif: ['Cormorant Garamond', 'serif'], sans: ['Inter', 'sans-serif'] }},
                    colors: {{ brandBg: '#F8F7F4', brandPrimary: '#111111', brandSecondary: '#6B7280', brandBorder: '#E5E7EB' }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ background-color: #F8F7F4; color: #111111; overflow-x: hidden; -webkit-tap-highlight-color: transparent; }}
        .glass-header {{ background-color: rgba(248, 247, 244, 0.8); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); }}
    </style>
</head>
<body class="font-sans antialiased">

    <header class="glass-header sticky top-0 z-50 border-b border-brandBorder">
        <div class="max-w-[1400px] mx-auto px-6 h-24 flex items-center justify-between">
            <a href="index.html" class="flex flex-col py-2">
                <span class="font-serif text-2xl tracking-widest font-medium uppercase leading-none block">LESSFORMORE</span>
                <span class="font-serif text-[10px] tracking-[0.25em] text-brandSecondary uppercase mt-1.5 block leading-none">Reviewed. Compared. Simplified.</span>
            </a>
            <a href="reviews.html" class="text-xs uppercase tracking-widest text-brandSecondary hover:text-brandPrimary font-medium">← Back to Catalog</a>
        </div>
    </header>

    <main class="max-w-[1200px] mx-auto px-4 sm:px-8 py-8">
        <div class="text-center mb-8 md:mb-12">
            <span class="text-xs uppercase tracking-[0.2em] font-medium text-brandSecondary block mb-2">Independent Review / {code}</span>
            <h1 class="font-serif text-3xl sm:text-5xl tracking-tight leading-none uppercase">{name}</h1>
        </div>

        <div class="max-w-[800px] mx-auto grid grid-cols-1 md:grid-cols-12 gap-6 items-start mb-16">
            
            <div class="md:col-span-7 flex flex-col gap-6 w-full">
                <div class="border border-brandBorder p-3 bg-white w-full shadow-sm">
                    <div class="bg-brandBg aspect-[9/16] overflow-hidden border border-brandBorder/40 relative">
                        <img src="{thumb_url}" alt="{name} Visual Profile Cover" class="w-full h-full object-cover">
                        <div class="absolute bottom-3 left-3 bg-brandPrimary/90 text-white text-[9px] tracking-widest uppercase px-2 py-1 font-medium">Fit Preview</div>
                    </div>
                </div>

                <div class="border border-brandBorder p-2 bg-white/40 w-full">
                    <div class="relative w-full overflow-hidden" style="padding-top: 177.77%;">
                        <iframe class="absolute top-0 left-0 bottom-0 right-0 w-full h-full shadow-inner" src="{embed_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
                    </div>
                </div>
            </div>

            <div class="md:col-span-5 w-full md:sticky md:top-32">
                <div class="border border-brandBorder p-6 bg-white w-full shadow-sm">
                    <span class="text-[9px] uppercase tracking-widest font-medium text-brandSecondary block mb-3 text-center">Verified Purchase Destination</span>
                    <a href="{affiliate}" target="_blank" rel="noopener noreferrer" class="min-h-[52px] w-full inline-flex items-center justify-center bg-brandPrimary text-white text-xs uppercase tracking-widest font-medium text-center active:bg-opacity-80 transition-all duration-200 mb-4">
                        Buy on {store}
                    </a>
                    <p class="text-[9px] text-brandSecondary uppercase tracking-wider font-light text-center leading-normal border-t border-brandBg pt-3">
                        *Independent evaluation. When you purchase through links on our site, we may earn an affiliate commission.
                    </p>
                </div>
            </div>

        </div>

        <section class="max-w-4xl mx-auto border-t border-brandBorder pt-12 mt-16 mb-12">
            <h3 class="font-serif text-lg uppercase tracking-wider text-center mb-8">Complete The Uniform Framework</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {recommendations_html}
            </div>
        </section>
    </main>

</body>
</html>
"""

# Compile loop with smart YouTube image generation hooks
for prod in products:
    raw_url = prod["yt"].strip().replace(" ", "")
    video_id = raw_url.split("/shorts/")[-1].split("?")[0]
    
    youtube_thumb = f"https://img.youtube.com/vi/{video_id}/hqdefault.jpg"
    bulletproof_embed = f"https://www.youtube.com/embed/{video_id}?autoplay=0&mute=0&rel=0&showinfo=0&playsinline=1&enablejsapi=1&origin=https://lessformore.in"
    
    if prod["category"] in ["Shirt", "T-Shirt"]:
        rec_items = [p for p in products if p["category"] in ["Jeans", "Trousers", "Pants"]][:3]
    else:
        rec_items = [p for p in products if p["category"] in ["Shirt", "T-Shirt"]][:3]
        
    rec_html = ""
    for r in rec_items:
        r_id = r["yt"].strip().replace(" ", "").split("/shorts/")[-1].split("?")[0]
        r_thumb = f"https://img.youtube.com/vi/{r_id}/hqdefault.jpg"
        
        rec_html += f"""
        <a href="review-{r['code'].lower()}.html" class="block bg-white border border-brandBorder p-3 hover:border-brandPrimary transition-all group shadow-sm">
            <div class="aspect-[9/16] bg-brandBg overflow-hidden mb-3 border border-brandBorder/30">
                <img src="{r_thumb}" class="w-full h-full object-cover group-hover:scale-[1.02] transition-transform duration-300">
            </div>
            <span class="text-[9px] font-mono tracking-widest text-brandSecondary block mb-1">{r['code']} / {r['category'].upper()}</span>
            <span class="text-xs font-medium uppercase tracking-wide block truncate text-brandPrimary">{r['name']}</span>
        </a>
        """
        
    page_content = review_template.replace("{ga_id}", GA_TRACKING_ID).format(
        code=prod["code"],
        name=prod["name"],
        thumb_url=youtube_thumb,
        embed_url=bulletproof_embed,
        affiliate=prod["affiliate"].strip(),
        store=prod["store"],
        recommendations_html=rec_html
    )
    
    with open(f"review-{prod['code'].lower()}.html", "w", encoding="utf-8") as f:
        f.write(page_content)

# -------------------------------------------------------------------------
# THE CENTRAL CATALOG INDEX ARCHITECTURE WITH INTERACTIVE LIVE FILTER BAR
# -------------------------------------------------------------------------
catalog_template = """<!DOCTYPE html>
<html lang="en">
<head>
    <script async src="https://www.googletagmanager.com/gtag/js?id={ga_id}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{ga_id}');
    </script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>The Review Catalog | LESSFORMORE</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    fontFamily: {{ serif: ['Cormorant Garamond', 'serif'], sans: ['Inter', 'sans-serif'] }},
                    colors: {{ brandBg: '#F8F7F4', brandPrimary: '#111111', brandSecondary: '#6B7280', brandBorder: '#E5E7EB' }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ background-color: #F8F7F4; color: #111111; -webkit-tap-highlight-color: transparent; }}
        .glass-header {{ background-color: rgba(248, 247, 244, 0.8); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); }}
        .filter-btn.active {{ border-color: #111111; color: #111111; font-weight: 500; }}
    </style>
</head>
<body class="font-sans antialiased">

    <header class="glass-header sticky top-0 z-50 border-b border-brandBorder">
        <div class="max-w-[1400px] mx-auto px-6 h-24 flex items-center justify-between">
            <a href="index.html" class="flex flex-col py-2">
                <span class="font-serif text-2xl tracking-widest font-medium uppercase leading-none block">LESSFORMORE</span>
                <span class="font-serif text-[10px] tracking-[0.25em] text-brandSecondary uppercase mt-1.5 block leading-none">Reviewed. Compared. Simplified.</span>
            </a>
        </div>
    </header>

    <main class="max-w-[1400px] mx-auto px-4 sm:px-8 py-12">
        <div class="text-center mb-12">
            <h1 class="font-serif text-4xl uppercase tracking-tight mb-4">The Configuration Catalog</h1>
            <p class="text-xs text-brandSecondary uppercase tracking-[0.15em]">Filtered Analysis Matrices Across All 23 Essential Clothing Silhouettes</p>
        </div>

        <div class="flex flex-wrap items-center justify-center gap-2 mb-12 max-w-3xl mx-auto px-2">
            <button onclick="filterCategory('all')" class="filter-btn active text-[11px] uppercase tracking-widest px-4 py-2 border border-brandBorder bg-white text-brandSecondary hover:border-brandPrimary transition-all">All Pieces</button>
            <button onclick="filterCategory('Shirt')" class="filter-btn text-[11px] uppercase tracking-widest px-4 py-2 border border-brandBorder bg-white text-brandSecondary hover:border-brandPrimary transition-all">Shirts</button>
            <button onclick="filterCategory('T-Shirt')" class="filter-btn text-[11px] uppercase tracking-widest px-4 py-2 border border-brandBorder bg-white text-brandSecondary hover:border-brandPrimary transition-all">T-Shirts</button>
            <button onclick="filterCategory('Jeans')" class="filter-btn text-[11px] uppercase tracking-widest px-4 py-2 border border-brandBorder bg-white text-brandSecondary hover:border-brandPrimary transition-all">Jeans</button>
            <button onclick="filterCategory('Trousers')" class="filter-btn text-[11px] uppercase tracking-widest px-4 py-2 border border-brandBorder bg-white text-brandSecondary hover:border-brandPrimary transition-all">Trousers</button>
            <button onclick="filterCategory('Pants')" class="filter-btn text-[11px] uppercase tracking-widest px-4 py-2 border border-brandBorder bg-white text-brandSecondary hover:border-brandPrimary transition-all">Pants</button>
            <button onclick="filterCategory('Shorts')" class="filter-btn text-[11px] uppercase tracking-widest px-4 py-2 border border-brandBorder bg-white text-brandSecondary hover:border-brandPrimary transition-all">Shorts</button>
            <button onclick="filterCategory('Footwear')" class="filter-btn text-[11px] uppercase tracking-widest px-4 py-2 border border-brandBorder bg-white text-brandSecondary hover:border-brandPrimary transition-all">Footwear</button>
        </div>

        <section id="product-grid" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
            {catalog_products_html}
        </section>
    </main>

    <script>
        function filterCategory(category) {{
            const buttons = document.querySelectorAll('.filter-btn');
            buttons.forEach(btn => btn.classList.remove('active'));
            event.target.classList.add('active');

            const cards = document.querySelectorAll('.product-card');
            cards.forEach(card => {{
                if (category === 'all' || card.getAttribute('data-category') === category) {{
                    card.style.display = 'flex';
                }} else {{
                    card.style.display = 'none';
                }}
            }});
        }}
    </script>

</body>
</html>
"""

catalog_html = ""
for prod in products:
    c_id = prod["yt"].strip().replace(" ", "").split("/shorts/")[-1].split("?")[0]
    c_thumb = f"https://img.youtube.com/vi/{c_id}/hqdefault.jpg"
    
    catalog_html += f"""
    <div class="product-card border border-brandBorder bg-white p-4 flex flex-col justify-between group hover:border-brandPrimary transition-all duration-300 shadow-sm" data-category="{prod['category']}">
        <div>
            <a href="review-{prod['code'].lower()}.html" class="block aspect-[9/16] bg-brandBg overflow-hidden mb-4 border border-brandBorder/30 relative">
                <img src="{c_thumb}" class="w-full h-full object-cover group-hover:scale-[1.01] transition-transform duration-300">
            </a>
            <div class="flex items-center justify-between mb-2">
                <span class="text-[10px] font-mono tracking-widest text-brandSecondary">{prod['code']}</span>
                <span class="text-[9px] uppercase tracking-widest bg-brandBg px-2 py-0.5 border border-brandBorder text-brandSecondary">{prod['category']}</span>
            </div>
            <h3 class="font-serif text-lg uppercase tracking-tight leading-tight mb-1 text-brandPrimary">{prod['name']}</h3>
            <span class="text-[10px] text-brandSecondary uppercase tracking-wider font-light">Via {prod['store']}</span>
        </div>
        <div class="flex items-center justify-between pt-4 border-t border-brandBg mt-4">
            <a href="review-{prod['code'].lower()}.html" class="text-xs uppercase tracking-widest font-medium text-brandPrimary hover:text-brandSecondary transition-colors">Analysis Profile →</a>
            <a href="{prod['affiliate'].strip()}" target="_blank" rel="noopener noreferrer" class="text-[10px] uppercase tracking-widest text-brandSecondary hover:text-brandPrimary transition-colors">Buy Link</a>
        </div>
    </div>
    """

with open("reviews.html", "w", encoding="utf-8") as f:
    f.write(catalog_template.replace("{ga_id}", GA_TRACKING_ID).format(catalog_products_html=catalog_html))

print("Success: Overhauled side-by-side grids, clickable thumbnail maps, and tracking systems across all assets!")