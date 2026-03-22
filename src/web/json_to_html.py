import json


def create_html():

    with open("data/json/result.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    matches = data["data"]["visual_matches"]
    organic = data["data"]["organic_results"]
    related = data["data"]["related_searches"]

    top = matches[2]   # main result

    html = f"""
    <html>
    <head>

    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>

    body{{
        margin:0;
        background:#202124;
        font-family:Arial;
        color:white;
        display:flex;
        justify-content:center;
    }}

    .phone{{
        width:400px;
        padding:12px;
    }}

    .header{{
        font-size:22px;
        padding:10px;
    }}

    .hero{{
        background:#303134;
        border-radius:12px;
        padding:12px;
        margin-bottom:16px;
        text-align:center;
    }}

    .hero img{{
        width:100%;
        height:260px;
        object-fit:contain;
        border-radius:12px;
        margin-bottom:10px;
        background:#202124;
    }}

    .hero-title{{
        font-size:20px;
        color:#8ab4f8;
    }}

    .card{{
        background:#303134;
        border-radius:12px;
        padding:12px;
        margin-bottom:14px;
        display:flex;
    }}

    .text{{
        flex:1;
    }}

    .logo{{
        width:18px;
        height:18px;
        margin-right:6px;
    }}

    .domain{{
        color:#9aa0a6;
        font-size:13px;
        display:flex;
        align-items:center;
    }}

    .title{{
        color:#8ab4f8;
        font-size:17px;
        margin:6px 0;
    }}

    .meta{{
        font-size:12px;
        color:#bdc1c6;
    }}

    .thumb{{
        width:110px;
        height:110px;
        border-radius:10px;
        object-fit:cover;
        margin-left:10px;
    }}

    .section{{
        font-size:18px;
        margin:15px 0 8px;
    }}

    .related{{
        background:#303134;
        padding:8px;
        border-radius:8px;
        margin-bottom:6px;
    }}

    a{{
        text-decoration:none;
        color:white;
    }}

    </style>

    </head>

    <body>

    <div class="phone">

    <div class="header">
    Reverse Image Results
    </div>

    <div class="hero">
        <img src="{top['image']}">
        <div class="hero-title">{top['title']}</div>
    </div>

    <div class="section">Visual Matches</div>
    """

    # VISUAL MATCHES
    for item in matches[:15]:

        rating = item.get("rating", "")
        reviews = item.get("reviews", "")

        html += f"""
        <a href="{item['link']}" target="_blank">

        <div class="card">

            <div class="text">

                <div class="domain">
                    <img class="logo" src="{item['source_icon']}">
                    {item['source']}
                </div>

                <div class="title">
                    {item['title']}
                </div>

                <div class="meta">
                    Position #{item['position']} •
                    {item['image_width']} × {item['image_height']}
                </div>

                <div class="meta">
                    ⭐ {rating} ({reviews} reviews)
                </div>

            </div>

            <img class="thumb" src="{item['thumbnail']}">

        </div>

        </a>
        """

    # ORGANIC RESULTS
    html += '<div class="section">Web Results</div>'

    for item in organic[:6]:

        html += f"""
        <div class="card">

            <div class="text">

                <div class="domain">
                    {item['domain']}
                </div>

                <div class="title">
                    <a href="{item['url']}" target="_blank">{item['title']}</a>
                </div>

                <div class="meta">
                    {item['snippet']}
                </div>

            </div>

        </div>
        """

    # RELATED SEARCHES
    html += '<div class="section">Related Searches</div>'

    for item in related:

        html += f"""
        <div class="related">
            {item['query']}
        </div>
        """

    html += """
    </div>
    </body>
    </html>
    """

    with open("src/web/templates/result.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("HTML page created: src/web/templates/result.html")
    