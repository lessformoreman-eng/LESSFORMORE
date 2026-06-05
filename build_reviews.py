import os

# Complete, clean dataset derived from your catalog
products = [
    {"code": "LFM001", "name": "Snitch Twilight Blue Shirt", "yt": "https://youtube.com/shorts/Pkz8ur6", "affiliate": "https://ajiio.in/Pkz8ur6", "store": "AJIO"},
    {"code": "LFM002", "name": "British Club Checked Slim Fit", "yt": "https://youtube.com/shorts/bqRMXnK", "affiliate": "https://ajiio.in/bqRMXnK", "store": "AJIO"},
    {"code": "LFM003", "name": "Bene Kleed Beige Boot Cut Jeans", "yt": "https://youtube.com/shorts/m6PDE1y", "affiliate": "https://ajiio.in/m6PDE1y", "store": "AJIO"},
    {"code": "LFM004", "name": "Campus Sutra ripped shirt", "yt": "https://youtube.com/shorts/g7LvJuF", "affiliate": "https://ajiio.in/g7LvJuF", "store": "AJIO"},
    {"code": "LFM005", "name": "The Bear House Men Checked", "yt": "https://youtube.com/shorts/dd4olF7", "affiliate": "https://ajiio.in/dd4olF7", "store": "AJIO"},
    {"code": "LFM006", "name": "BENE KLEED Men Mid Rise Jeans", "yt": "https://youtube.com/shorts/m6PDE1y", "affiliate": "https://ajiio.in/m6PDE1y", "store": "AJIO"},
    {"code": "LFM007", "name": "TEAMSPIRIT Men Regular Fit Polo T-Shirt", "yt": "https://youtube.com/shorts/Th0DPJ1", "affiliate": "https://ajiio.in/Th0DPJ1", "store": "AJIO"},
    {"code": "LFM008", "name": "Sparx Men Textured Thong Flip-Flop", "yt": "https://youtube.com/shorts/6FVQ6kG", "affiliate": "https://myntr.it/6FVQ6kG", "store": "Myntra"},
    {"code": "LFM009", "name": "KOTTY Men Man Regular Fit Jeans", "yt": "https://youtube.com/shorts/6y15L4D", "affiliate": "https://ajiio.in/6y15L4D", "store": "AJIO"},
    {"code": "LFM010", "name": "TEAMSPIRIT Men Straight Fit Track Pants", "yt": "https://youtube.com/shorts/OfxykxE", "affiliate": "https://ajiio.in/OfxykxE", "store": "AJIO"},
    {"code": "LFM011", "name": "YOUSTA Men Low-Top Lace-Up Sneakers", "yt": "https://youtube.com/shorts/c1YyGIC", "affiliate": "https://ajiio.in/c1YyGIC", "store": "AJIO"},
    {"code": "LFM012", "name": "HERE&NOW Men Opaque Casual Shirt", "yt": "https://youtube.com/shorts/P4K2tZm", "affiliate": "https://myntr.it/P4K2tZm", "store": "Myntra"},
    {"code": "LFM013", "name": "PERFORMAX Ultra Lightweight Fastdry T-Shirt", "yt": "https://youtube.com/shorts/QHdsiN7", "affiliate": "https://ajiio.in/QHdsiN7", "store": "AJIO"},
    {"code": "LFM014", "name": "HRX by Hrithik Roshan Men Mesh Shoes", "yt": "https://youtube.com/shorts/VbA6YO3", "affiliate": "https://myntr.it/VbA6YO3", "store": "Myntra"},
    {"code": "LFM015", "name": "LEE COOPER Men Regular Fit Shirt", "yt": "https://youtube.com/shorts/1BXhxvy", "affiliate": "https://ajiio.in/1BXhxvy", "store": "AJIO"},
    {"code": "LFM016", "name": "ARROW Men Tapered Fit Trousers", "yt": "https://youtube.com/shorts/hm8nlwt", "affiliate": "https://ajiio.in/hm8nlwt", "store": "AJIO"},
    {"code": "LFM017", "name": "PERFORMAX Men Regular Fit Crew-Neck T-Shirt", "yt": "https://youtube.com/shorts/7xY81kA", "affiliate": "https://ajiio.in/7xY81kA", "store": "AJIO"},
    {"code": "LFM018", "name": "PUMA Men's Slim Fit Polo T-Shirt", "yt": "https://youtube.com/shorts/NelSc1y", "affiliate": "https://ajiio.in/NelSc1y", "store": "AJIO"},
    {"code": "LFM019", "name": "KAPPA Regular Fit Polo T-Shirt", "yt": "https://youtube.com/shorts/8em6eJH", "affiliate": "https://ajiio.in/8em6eJH", "store": "AJIO"},
    {"code": "LFM020", "name": "PERFORMAX Men Dual-Strap Sandals", "yt": "https://youtube.com/shorts/A6cLnxR", "affiliate": "https://ajiio.in/A6cLnxR", "store": "AJIO"},
    {"code": "LFM021", "name": "SNITCH Men Lightly-Washed Straight Jeans", "yt": "https://youtube.com/shorts/s1OUunX", "affiliate": "https://ajiio.in/s1OUunX", "store": "AJIO"},
    {"code": "LFM022", "name": "PERFORMAX Men Regular Fit Shorts", "yt": "https://youtube.com/shorts/Ouusp9r", "affiliate": "https://ajiio.in/Ouusp9r", "store": "AJIO"},
    {"code": "LFM023", "name": "Dockstreet Men Striped Black Trackpant", "yt": "https://youtube.com/shorts/0uGo7te", "affiliate": "https://fktr.in/0uGo7te", "store": "Flipkart"}
]

html_template = """<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
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
        .contain-product-img {{ object-fit: contain; width: 100%; height: 100%; max-height: 70vh; }}
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

    <main class="max-w-[1200px] mx-auto px-4 sm:px-8 py-8">
        <div class="text-center mb-8 md:mb-12">
            <span class="text-xs uppercase tracking-[0.2em] font-medium text-brandSecondary block mb-2">Independent Review / {code}</span>
            <h1 class="font-serif text-3xl sm:text-5xl tracking-tight leading-none uppercase">{name}</h1>
        </div>

        <!-- TWO-COLUMN SECTION FOR VIDEO AND BUY MODULE (Brings Button Directly to Top-Fold) -->
        <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-start mb-12 max-w-4xl mx-auto">
            
            <!-- Video Column Block -->
            <div class="md:col-span-7 border border-brandBorder p-2 bg-white/40 w-full max-w-[340px] mx-auto md:max-w-none">
                <div class="relative w-full overflow-hidden" style="padding-top: 177.77%;">
                    <iframe class="absolute top-0 left-0 bottom-0 right-0 w-full h-full" src="{embed_url}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                </div>
            </div>

            <!-- Transaction Link Column Block (Placed Directly Below/Right of Video Block) -->
            <div class="md:col-span-5 border border-brandBorder p-6 sm:p-8 bg-white w-full max-w-[340px] mx-auto md:max-w-none">
                <span class="text-[9px] uppercase tracking-widest font-medium text-brandSecondary block mb-4 text-center">Verified Purchase Destination</span>
                <a href="{affiliate}" target="_blank" rel="noopener noreferrer" class="min-h-[52px] w-full inline-flex items-center justify-center bg-brandPrimary text-white text-xs uppercase tracking-widest font-medium text-center active:bg-opacity-80 transition-all duration-200">
                    Buy on {store}
                </a>
                <p class="text-[9px] text-brandSecondary font-light leading-relaxed tracking-wide mt-6 pt-4 border-t border-brandBorder text-center">
                    This page contains affiliate links. We may earn a commission if you purchase through these links.
                </p>
            </div>
        </div>

        <!-- Product Image Showcase Layout - Preserves clothing silhouette proportions completely -->
        <section class="max-w-4xl mx-auto mb-12">
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 bg-white/30 border border-brandBorder p-4">
                <div class="flex items-center justify-center bg-brandBg p-2 aspect-[3/4]">
                    <img src="images/{code}-front.jpg" alt="Front View" class="contain-product-img" onerror="this.src='https://images.unsplash.com/photo-1541099649105-f69ad21f3246?q=80&w=800&auto=format&fit=crop'">
                </div>
                <div class="flex items-center justify-center bg-brandBg p-2 aspect-[3/4]">
                    <img src="images/{code}-detail.jpg" alt="Detail View" class="contain-product-img" onerror="this.src='https://images.unsplash.com/photo-1542272604-787c3835535d?q=80&w=800&auto=format&fit=crop'">
                </div>
            </div>
        </section>
    </main>

</body>
</html>
"""

for prod in products:
    # Explicit URL sanitation framework to avoid standard rendering error 153
    video_id = prod["yt"].strip().split("/")[-1]
    cleaned_embed = f"https://www.youtube.com/embed/{video_id}"
    
    page_content = html_template.format(
        code=prod["code"],
        name=prod["name"],
        embed_url=cleaned_embed,
        affiliate=prod["affiliate"].strip(),
        store=prod["store"]
    )
    
    filename = f"review-{prod['code'].lower()}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(page_content)

print(f"Success: Successfully processed {len(products)} fixed pages layout structures!")
