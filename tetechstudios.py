# fake_hack_show_fullscreen_hidden_exit.py
# Tam ekran "hacker intro" gösterisi — gizli çıkış
# - Triple-tap veya uzunca basma ile çıkış (gizli alan: sol üst köşe)
# - GitHub Aç butonu görünür (dokunmatik uyumlu)
# - SAFE: hiçbir gerçek hack işlemi yapmaz

import pygame, sys, random, time, math, webbrowser

# ---------- Ayarlar ----------
USE_FULLSCREEN = True   # True = tam ekran, False = pencere
AUTO_TIMEOUT_SECONDS = 0  # 0 = devre dışı, >0 süre sonra otomatik kapanır

# Gizli çıkış bölgesi ve ayarlar
HIDDEN_AREA_SIZE = 30  # px (sol üst köşe)
TRIPLE_TAP_WINDOW = 1.5  # saniye içinde 3 tıklama
LONG_PRESS_SECONDS = 1.5  # uzun basma süresi (saniye)

# ---------- Pygame başlat ----------
pygame.init()
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h if USE_FULLSCREEN else (1280, 720)
flags = pygame.FULLSCREEN if USE_FULLSCREEN else 0
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags)
pygame.display.set_caption("H4CK3R SHOW - TETech Edition (Fullscreen)")
clock = pygame.time.Clock()
FPS = 60

# Renkler
BLACK = (0,0,0)
GREEN = (0,255,70)
DIM_GREEN = (0,180,50)
WHITE = (255,255,255)
GRAY = (40,40,40)
BUTTON_RED = (180, 30, 30)
BUTTON_GREEN = (30, 180, 30)

# Fontlar: sistem uyumlu seçelim
mono = pygame.font.SysFont("consolas", max(16, WIDTH//80))
big = pygame.font.SysFont("consolas", max(32, WIDTH//40))
title_font = pygame.font.SysFont("consolas", max(64, WIDTH//20), bold=True)
btn_font = pygame.font.SysFont("consolas", max(20, WIDTH//60))

# Helper
def rand_ip():
    return "{}.{}.{}.{}".format(*(random.randint(1,254) for _ in range(4)))
def fake_hash():
    return ''.join(random.choice("0123456789abcdef") for _ in range(32))

# Matrix rain
cols = max(40, WIDTH // 14)
drops = [random.randint(-HEIGHT, 0) for _ in range(cols)]

# Logs + typing
log_lines = []
max_logs = 30
typing_active = None
typing_pos = 0
typing_speed = 0.008
last_typing_time = 0

commands = [
    "nmap -sS {} -p 1-65535".format(rand_ip()),
    "ssh user@{}".format(rand_ip()),
    "curl -s http://{}:8080/get_flag".format(rand_ip()),
    "python exploit.py --target {}".format(rand_ip()),
    "git clone https://github.com/some/repo.git",
    "deploy --force --env=prod",
    "running exploit chain...",
]

def push_log(s):
    if len(log_lines) >= max_logs:
        log_lines.pop(0)
    log_lines.append(s)

def start_typing(text):
    global typing_active, typing_pos, last_typing_time
    typing_active = text
    typing_pos = 0
    last_typing_time = time.time()

# Başlangıç logları
push_log("Initializing secure terminal...")
push_log("Kernel modules loaded.")
push_log("Network interfaces up: eth0 wlan0")
push_log("Setting stealth mode: ON")
start_typing("sudo ./run_super_exploit --stealth")

# Partikül sistemi
class Particle:
    def __init__(self, x, y):
        self.x = x + random.randint(-int(WIDTH*0.02), int(WIDTH*0.02))
        self.y = y + random.randint(-10, int(HEIGHT*0.03))
        self.size = random.randint(max(1, WIDTH//500), max(2, WIDTH//300))
        self.speed_y = random.uniform(-0.5, -1.5)
        self.alpha = 255
        self.color = (random.randint(150,255), 255, random.randint(150,255))
    def update(self):
        self.y += self.speed_y
        self.alpha -= 3
    def draw(self, surf):
        s = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA, 32)
        pygame.draw.circle(s, (*self.color, max(self.alpha,0)), (self.size,self.size), self.size)
        surf.blit(s, (self.x, self.y))

particles = []

def draw_title_and_particles():
    title_text = "TETech Studios"
    pulse = (math.sin(time.time() * 2.5) + 1) / 2
    glow = 200 + int(55 * pulse)
    title_color = (glow, glow, glow)
    shadow_color = (20, 20, 20)
    title_x = (WIDTH - title_font.size(title_text)[0]) // 2
    title_y = max(20, HEIGHT//40)

    # Outline (gölge)
    outline_range = 3 if WIDTH>1000 else 2
    for ox in range(-outline_range, outline_range+1):
        for oy in range(-outline_range, outline_range+1):
            if ox==0 and oy==0: continue
            shadow_surf = title_font.render(title_text, True, shadow_color)
            screen.blit(shadow_surf, (title_x + ox, title_y + oy))

    # Ana yazı
    title_surf = title_font.render(title_text, True, title_color)
    screen.blit(title_surf, (title_x, title_y))

    # Halo (hafif parlama)
    halo_surf = title_font.render(title_text, True, (100+int(155*pulse), 255, 100+int(155*pulse)))
    halo_surf.set_alpha(60)
    screen.blit(halo_surf, (title_x-2, title_y-2))

    # Alt başlık
    subtitle = "Live demo | zero harm"
    sub_surf = big.render(subtitle, True, (150, 255, 180))
    sub_x = (WIDTH - sub_surf.get_width()) // 2
    screen.blit(sub_surf, (sub_x, title_y + title_surf.get_height() + 6))

    # Partiküller üret
    if random.random() < 0.30:
        particles.append(Particle(title_x + title_surf.get_width()//2, title_y + title_surf.get_height()//2))
    for p in particles[:]:
        p.update()
        p.draw(screen)
        if p.alpha <= 0:
            particles.remove(p)

# Buton çizim fonksiyonu (dokunmatik uygun)
def draw_button(text, x, y, w, h, color_bg, color_text=WHITE):
    pygame.draw.rect(screen, (10,10,10), (x-6,y-6,w+12,h+12), border_radius=8)  # hafif arka çerçeve
    pygame.draw.rect(screen, color_bg, (x,y,w,h), border_radius=8)
    label = btn_font.render(text, True, color_text)
    label_rect = label.get_rect(center=(x + w/2, y + h/2))
    screen.blit(label, label_rect)
    return pygame.Rect(x, y, w, h)

# Gizli-çıkış kontrol değişkenleri
hidden_taps = []
hidden_press_start = None

# Zamanlama
start_time = time.time()
running = True
open_github = False

# Main loop
while running:
    dt = clock.tick(FPS)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

        # Mouse / touch press
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my = event.pos
            # Gizli çıkış alanı (sol üst köşe)
            if 0 <= mx <= HIDDEN_AREA_SIZE and 0 <= my <= HIDDEN_AREA_SIZE:
                # kaydet tap zamanı
                hidden_taps.append(time.time())
                # temizle eski tapleri
                now = time.time()
                hidden_taps = [t for t in hidden_taps if now - t <= TRIPLE_TAP_WINDOW]
                if len(hidden_taps) >= 3:
                    # üçlü tap tespit edildi
                    running = False
                # uzun basma için zamanı başlat
                hidden_press_start = time.time()

            # Visible butonlar: GitHub
            panel_w = int(WIDTH*0.6)
            panel_x = WIDTH - panel_w - 20
            btn_y = HEIGHT - 110
            github_x = panel_x + 10
            github_w = int(panel_w*0.25)
            github_rect = pygame.Rect(github_x, btn_y, github_w, 56)
            if github_rect.collidepoint((mx,my)):
                open_github = True
                running = False

        if event.type == pygame.MOUSEBUTTONUP:
            # uzun basma kontrolü
            if hidden_press_start is not None:
                held = time.time() - hidden_press_start
                hidden_press_start = None
                if held >= LONG_PRESS_SECONDS:
                    running = False

        # Klavye (yine yedek): ESC veya SPACE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                open_github = True
                running = False

    # Otomatik zaman aşımı (isteğe bağlı)
    if AUTO_TIMEOUT_SECONDS > 0 and (time.time() - start_time) > AUTO_TIMEOUT_SECONDS:
        running = False

    screen.fill(BLACK)

    # Matrix rain
    col_width = max(12, WIDTH // cols)
    for i in range(cols):
        x = i * col_width
        drop_y = drops[i]
        for j in range(10):
            char = random.choice("01{}{}".format("ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz"))
            y = drop_y - j*14
            if 0 <= y < HEIGHT:
                color = DIM_GREEN if j>2 else GREEN
                screen.blit(mono.render(char, True, color), (x, y))
        drops[i] += int(300*dt)
        if drops[i] > HEIGHT + random.randint(0,200):
            drops[i] = random.randint(-1000,0)

    # Sağ panel
    panel_w = int(WIDTH*0.6)
    panel_x = WIDTH - panel_w - 20
    pygame.draw.rect(screen, (10,10,10), (panel_x, 20, panel_w, HEIGHT-40), border_radius=6)
    screen.blit(big.render("root@terminal:~#", True, GREEN), (panel_x + 10, 30))

    # Typing efekt
    global_typing = globals()
    if typing_active:
        now = time.time()
        if typing_pos < len(typing_active):
            if now - last_typing_time >= typing_speed:
                typing_pos += 1
                last_typing_time = now
            display = typing_active[:typing_pos] + ("_" if int(now*2)%2==0 else " ")
        else:
            display = typing_active
            push_log("[OK] " + typing_active)
            typing_active = None
            if random.random() < 0.6:
                start_typing(random.choice(commands))
            else:
                push_log("[INFO] background processes running.")
        screen.blit(mono.render(display, True, GREEN), (panel_x + 10, 100))
    else:
        if random.random() < 0.01:
            start_typing(random.choice(commands))

    # Loglar
    y0 = 150
    for i, ln in enumerate(reversed(log_lines)):
        txt = mono.render(ln, True, GREEN)
        screen.blit(txt, (panel_x + 10, y0 + i* (max(18, HEIGHT//40))))

    # Progress bar
    prog_fraction = ((time.time() - start_time)/12.0) % 1.0
    pb_x = panel_x + 10
    pb_y = HEIGHT - 150
    pb_w = int(panel_w) - 40
    pygame.draw.rect(screen, GRAY, (pb_x, pb_y, pb_w, max(18, HEIGHT//40)))
    pygame.draw.rect(screen, GREEN, (pb_x, pb_y, int(pb_w*prog_fraction), max(18, HEIGHT//40)))
    screen.blit(mono.render("Transferring payload... {}%".format(int(prog_fraction*100)), True, WHITE), (pb_x, pb_y- (max(18, HEIGHT//40) + 6)))

    # IP & session
    iptxt = mono.render("SRC IP: {}".format(rand_ip()), True, GREEN)
    htxt = mono.render("SESSION: {}".format(fake_hash()), True, GREEN)
    screen.blit(iptxt, (panel_x+10, HEIGHT-110))
    screen.blit(htxt, (panel_x+10, HEIGHT-90))

    # Hint (küçük)
    hint = mono.render("Dokunmatik alan: sol-üst gizli (3 kere kısa bas veya 1.5s basılı tut). Buton: GitHub Aç.", True, WHITE)
    screen.blit(hint, (30, HEIGHT-40))

    # Başlık + partiküller (önde)
    draw_title_and_particles()

    # Visible buton: GitHub Aç
    btn_y = HEIGHT - 110
    github_x = panel_x + 10
    github_w = int(panel_w*0.25)
    github_rect = draw_button("GitHub Aç", github_x, btn_y, github_w, 56, BUTTON_GREEN)

    # (Gizli alan görsel gösterge HDEBUG için; normalde yorum satırında kalsın)
    # Uncomment the following line to debug the hidden area (draw a semi-transparent rect)
    # pygame.draw.rect(screen, (255,0,0,50), (0,0,HIDDEN_AREA_SIZE,HIDDEN_AREA_SIZE), 1)

    pygame.display.flip()

# Tarayıcı aç
if open_github:
    webbrowser.open("https://github.com")

pygame.quit()
sys.exit()
