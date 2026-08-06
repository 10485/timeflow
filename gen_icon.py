from PIL import Image, ImageDraw
import math

def make_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # 深色圆底
    r = size // 2 - 6
    cx, cy = size // 2, size // 2
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(15, 15, 20, 255))

    # 外环（极光蓝）
    ring_w = max(4, size // 40)
    draw.ellipse([cx - r + ring_w, cy - r + ring_w, cx + r - ring_w, cy + r - ring_w],
                 outline=(59, 130, 246, 255), width=ring_w)

    # 刻度线
    for i in range(12):
        angle = math.radians(i * 30 - 90)
        outer = r - ring_w - max(3, size // 60)
        inner = outer - max(6, size // 30) if i % 3 == 0 else outer - max(3, size // 50)
        x1 = cx + math.cos(angle) * outer
        y1 = cy + math.sin(angle) * outer
        x2 = cx + math.cos(angle) * inner
        y2 = cy + math.sin(angle) * inner
        clr = (59, 130, 246, 255) if i % 3 == 0 else (255, 255, 255, 120)
        draw.line([x1, y1, x2, y2], fill=clr, width=max(1, size // 150))

    # 时针（粗）
    h = math.radians(310)  # ~10:20 经典位置
    h_len = r * 0.45
    hx = cx + math.cos(h) * h_len
    hy = cy + math.sin(h) * h_len
    draw.line([cx, cy, hx, hy], fill=(255, 255, 255, 230), width=max(3, size // 50))

    # 分针（细长）
    m = math.radians(110)
    m_len = r * 0.65
    mx = cx + math.cos(m) * m_len
    my = cy + math.sin(m) * m_len
    draw.line([cx, cy, mx, my], fill=(59, 130, 246, 230), width=max(2, size // 80))

    # 中心点
    dr = max(2, size // 60)
    draw.ellipse([cx - dr, cy - dr, cx + dr, cy + dr], fill=(59, 130, 246, 255))

    return img

make_icon(192).save('icon-192.png', 'PNG')
make_icon(512).save('icon-512.png', 'PNG')
print("Icons generated: icon-192.png, icon-512.png")
