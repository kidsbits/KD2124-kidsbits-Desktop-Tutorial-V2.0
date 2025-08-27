import time
import framebuf

class SSH1106:
    def __init__(self, i2c, width, height, addr=0x3C):
        self.i2c = i2c
        self.addr = addr
        self.width = width
        self.height = height
        self.pages = height // 8
        self.buffer = bytearray(self.pages * width)
        self.fb = framebuf.FrameBuffer(self.buffer, width, height, framebuf.MONO_VLSB)
        self.init_display()

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, bytearray([0x00, cmd]))

    def init_display(self):
        for cmd in (
            0xAE,  # Display off
            0xA8, 0x3F,  # Set multiplex ratio (1 to 64)
            0xD3, 0x00,  # Set display offset
            0x40,  # Set start line address
            0xA1,  # Set segment re-map 0 to 127
            0xC8,  # Set COM output scan direction
            0xDA, 0x12,  # Set COM pins hardware configuration
            0x81, 0xCF,  # Set contrast control
            0xD9, 0xF1,  # Set pre-charge period
            0xDB, 0x40,  # Set VCOMH deselect level
            0xA4,  # Enable display RAM content
            0xA6,  # Set normal display mode (not inverted)
            0x20, 0x00,  # Set memory addressing mode to horizontal
            0xAF,  # Display on
        ):
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def poweroff(self):
        self.write_cmd(0xAE)

    def poweron(self):
        self.write_cmd(0xAF)

    def contrast(self, contrast):
        self.write_cmd(0x81)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(0xA6 | (invert & 1))

    def show(self):
        for page in range(self.pages):
            self.write_cmd(0xB0 + page)
            self.write_cmd(0x00)
            self.write_cmd(0x10)
            self.i2c.writeto(self.addr, bytearray([0x40]) + self.buffer[page * self.width:(page + 1) * self.width])

    def fill(self, color):
        self.fb.fill(color)

    def pixel(self, x, y, color):
        self.fb.pixel(x, y, color)

    def text(self, text, x, y, color=1):
        self.fb.text(text, x, y, color)

    def hline(self, x, y, w, color):
        self.fb.hline(x, y, w, color)

    def vline(self, x, y, h, color):
        self.fb.vline(x, y, h, color)

    def rect(self, x, y, w, h, color):
        self.fb.rect(x, y, w, h, color)

    def fill_rect(self, x, y, w, h, color):
        self.fb.fill_rect(x, y, w, h, color)

    def scroll(self, dx, dy):
        self.fb.scroll(dx, dy)

    def blit(self, framebuffer, x, y):
        self.fb.blit(framebuffer, x, y)

