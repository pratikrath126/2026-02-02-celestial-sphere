with open("index.html", "r") as f:
    content = f.read()

import re

# We will replace the <img> tag representing the static art with a <canvas> element.
content = re.sub(
    r'<img class="absolute[^>]*src="[^"]*".*?/>',
    '<canvas id="starfield" class="absolute w-full h-full object-contain opacity-90 rounded-full"></canvas>',
    content
)

# And add the starfield script right before </body>
script = """
<script>
    const canvas = document.getElementById('starfield');
    const ctx = canvas.getContext('2d');

    let width, height;
    let stars = [];

    function resize() {
        const parent = canvas.parentElement;
        // make sure canvas internal resolution matches display size
        const rect = parent.getBoundingClientRect();
        width = canvas.width = rect.width;
        height = canvas.height = rect.height;
    }

    class Star {
        constructor() {
            this.reset();
        }

        reset() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.z = Math.random() * width;
            this.pz = this.z;
        }

        update() {
            this.z -= 2; // speed
            if (this.z < 1) {
                this.reset();
                this.pz = this.z;
            }
        }

        draw() {
            let sx = (this.x - width / 2) * (width / this.z) + width / 2;
            let sy = (this.y - height / 2) * (width / this.z) + height / 2;

            let px = (this.x - width / 2) * (width / this.pz) + width / 2;
            let py = (this.y - height / 2) * (width / this.pz) + height / 2;

            this.pz = this.z;

            // Optional bounds check to avoid drawing way outside
            if (sx < 0 || sx > width || sy < 0 || sy > height) return;

            ctx.beginPath();
            ctx.strokeStyle = "rgba(255, 255, 255, " + (1 - this.z / width) + ")";
            ctx.lineWidth = Math.max(0.1, (1 - this.z / width) * 2);
            ctx.moveTo(px, py);
            ctx.lineTo(sx, sy);
            ctx.stroke();
        }
    }

    function init() {
        resize();
        window.addEventListener('resize', resize);
        for (let i = 0; i < 400; i++) {
            stars.push(new Star());
        }
        requestAnimationFrame(animate);
    }

    function animate() {
        ctx.fillStyle = "rgba(11, 9, 21, 0.2)"; // dark background with trail effect
        ctx.fillRect(0, 0, width, height);

        // draw a subtle inner clip path to stay inside the circle if needed,
        // actually since the canvas is rounded-full, css will clip it.

        stars.forEach(star => {
            star.update();
            star.draw();
        });
        requestAnimationFrame(animate);
    }

    // Give layout time to settle, or use a ResizeObserver in real life.
    setTimeout(init, 100);
</script>
"""

content = content.replace("</body>", script + "\n</body>")

with open("index.html", "w") as f:
    f.write(content)
