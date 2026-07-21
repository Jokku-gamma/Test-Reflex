import reflex as rx
from reflex.components.component import NoSSRComponent

# ==========================================
# 1. REACT WRAPPERS (Spline 3D & Framer Motion)
# ==========================================

class SplineScene(NoSSRComponent):
    """React Spline wrapper for rendering interactive 3D scenes."""
    library = "@splinetool/react-spline"
    lib_dependencies = ["@splinetool/runtime"]
    tag = "Spline"
    is_default = True
    scene: rx.Var[str]

spline = SplineScene.create


class MotionDiv(rx.Component):
    """Framer Motion wrapper for smooth component animations."""
    library = "framer-motion"
    tag = "motion.div"
    is_default = False
    
    initial: rx.Var[dict]
    animate: rx.Var[dict]
    transition: rx.Var[dict]
    whileHover: rx.Var[dict]
    whileTap: rx.Var[dict]

motion_div = MotionDiv.create


# ==========================================
# 2. ANIMATION HELPERS & UI COMPONENTS
# ==========================================

def glowing_orb(color: str, top: str, left: str, delay: float):
    """Creates a massive blurred background sphere that pulses infinitely."""
    return motion_div(
        rx.box(
            width="40vw", 
            height="40vw",
            background=color,
            border_radius="50%",
            filter="blur(150px)",
            opacity="0.35",
            pointer_events="none",
        ),
        position="absolute", 
        top=top, 
        left=left, 
        z_index="0",
        initial={"scale": 0.8, "opacity": 0.15},
        animate={"scale": [0.8, 1.25, 0.8], "opacity": [0.15, 0.45, 0.15]},
        transition={"duration": 8, "repeat": 999, "delay": delay, "ease": "easeInOut"}
    )


def feature_card(icon: str, title: str, description: str):
    """Creates an animated glassmorphism feature card."""
    return motion_div(
        rx.vstack(
            rx.text(icon, font_size="2.5rem", margin_bottom="0.5rem"),
            rx.text(title, weight='bold', font_size="1.25rem", color="gray"),
            rx.text(description, color="rgba(255, 255, 255, 0.7)", font_size="0.95rem", line_height="1.5"),
            background="rgba(255, 255, 255, 0.03)",
            backdrop_filter="blur(16px)",
            border="1px solid rgba(79, 184, 255, 0.2)",
            padding="2em",
            border_radius="16px",
            spacing="3",
            align_items="flex-start",
            box_shadow="0 8px 32px 0 rgba(0, 0, 0, 0.37)",
            height="100%",
        ),
        initial={"opacity": 0, "y": 30},
        animate={"opacity": 1, "y": 0},
        transition={"duration": 0.8},
        whileHover={"scale": 1.04, "borderColor": "rgba(79, 184, 255, 0.6)", "boxShadow": "0 12px 40px rgba(0, 217, 255, 0.25)"}
    )


def stats_badge(label: str, value: str):
    """Displays a key performance metric badge."""
    return rx.vstack(
        rx.text(value, font_size="2.2rem", weight='bold', color="#00d9ff"),
        rx.text(label, font_size="0.85rem", color="gray.400", letter_spacing="0.05em", text_transform="uppercase"),
        align_items="center",
        padding="1rem 1.5rem",
        background="rgba(255, 255, 255, 0.02)",
        border="1px solid rgba(255, 255, 255, 0.08)",
        border_radius="12px",
        backdrop_filter="blur(8px)",
    )


def project_card(title: str, category: str, description: str, tags: list):
    """Displays a featured portfolio project card."""
    return motion_div(
        rx.vstack(
            rx.hstack(
                rx.badge(category, color_scheme="cyan", variant="solid", radius="full"),
                rx.spacer(),
                rx.text("↗", font_size="1.2rem", color="cyan.400"),
                width="100%",
                align_items="center"
            ),
            rx.heading(title, size="5", color="gray", margin_top="0.5rem"),
            rx.text(description, color="gray.400", font_size="0.9rem"),
            rx.hstack(
                *[rx.badge(t, variant="outline", color_scheme="gray") for t in tags],
                spacing="2",
                wrap="wrap",
                margin_top="1rem"
            ),
            background="rgba(15, 20, 32, 0.6)",
            border="1px solid rgba(0, 217, 255, 0.15)",
            backdrop_filter="blur(12px)",
            padding="1.8rem",
            border_radius="16px",
            spacing="3",
            width="100%",
        ),
        whileHover={"y": -6, "borderColor": "rgba(255, 0, 110, 0.5)", "boxShadow": "0 10px 30px rgba(255, 0, 110, 0.2)"},
        transition={"duration": 0.3}
    )


# ==========================================
# 3. MAIN LANDING PAGE
# ==========================================

def index() -> rx.Component:
    """Personal welcome landing page for Jokku."""
    return rx.box(
        # Glowing Animated Orbs Layer
        glowing_orb("#4fb8ff", top="-10%", left="10%", delay=0),
        glowing_orb("#ff006e", top="35%", left="65%", delay=2),
        glowing_orb("#00d9ff", top="65%", left="5%", delay=4),
        glowing_orb("#7928ca", top="85%", left="70%", delay=6),
        
        # 3D Spline Interactive Layer
        rx.box(
            spline(scene="https://prod.spline.design/joLpOOYbGL-10EJ4/scene.splinecode"),
            position="absolute", 
            top="0", 
            left="0", 
            width="100%", 
            height="100%", 
            z_index="1",
            opacity="0.75"
        ),
        
        # Floating Top Navigation Bar
        rx.hstack(
            rx.hstack(
                rx.box(
                    width="12px", height="12px", 
                    background="#00d9ff", 
                    border_radius="50%", 
                    box_shadow="0 0 10px #00d9ff"
                ),
                rx.text("JOKKU", weight='bold', letter_spacing="0.2em", color="gray", font_size="1.1rem"),
                spacing="3",
                align_items="center"
            ),
            rx.spacer(),
            rx.hstack(
                rx.link("Features", href="#features", color="gray.300", _hover={"color": "#00d9ff"}),
                rx.link("Work", href="#work", color="gray.300", _hover={"color": "#00d9ff"}),
                rx.link("Contact", href="#contact", color="gray.300", _hover={"color": "#00d9ff"}),
                spacing="6",
                display=["none", "none", "flex"]
            ),
            rx.spacer(),
            rx.badge("🟢 Available for Projects", color_scheme="green", variant="solid", radius="full", padding="0.4rem 0.8rem"),
            width="100%",
            padding="1.5rem 5%",
            position="fixed",
            top="0",
            left="0",
            z_index="20",
            backdrop_filter="blur(12px)",
            background="rgba(5, 5, 5, 0.4)",
            border_bottom="1px solid rgba(255, 255, 255, 0.05)"
        ),
        
        # Hero Welcome Section
        rx.center(
            rx.vstack(
                motion_div(
                    rx.badge(
                        "✨ Next-Gen Cyber Aesthetics & 3D Web",
                        variant="solid",
                        color_scheme="cyan",
                        font_size="0.85rem",
                        padding="0.5rem 1rem",
                        border_radius="9999px"
                    ),
                    initial={"opacity": 0, "y": -20},
                    animate={"opacity": 1, "y": 0},
                    transition={"duration": 0.8, "ease": "easeOut"}
                ),
                
                motion_div(
                    rx.text(
                        "Hi, I'm", 
                        font_size="1.5rem", 
                        weight="light", 
                        letter_spacing="0.15em", 
                        color="gray.400",
                        margin_top="1rem"
                    ),
                    initial={"opacity": 0, "y": -10},
                    animate={"opacity": 1, "y": 0},
                    transition={"duration": 0.8, "delay": 0.1}
                ),
                
                motion_div(
                    rx.heading(
                        "Jokku",
                        weight='bold',
                        style={
                            "font-size": "min(14vw, 9.5rem)",
                            "background": "linear-gradient(135deg, #4fb8ff 0%, #00d9ff 40%, #ff006e 100%)",
                            "-webkit-background-clip": "text",
                            "-webkit-text-fill-color": "transparent",
                            "line-height": "1",
                            "letter-spacing": "-0.03em",
                            "filter": "drop-shadow(0 0 45px rgba(79, 184, 255, 0.4))"
                        }
                    ),
                    initial={"opacity": 0, "scale": 0.85},
                    animate={"opacity": 1, "scale": 1},
                    transition={"duration": 1.2, "delay": 0.2, "ease": [0.16, 1, 0.3, 1]}
                ),
                
                motion_div(
                    rx.text(
                        "Welcome to my interactive world of code, motion, and 3D experiences.",
                        font_size="1.25rem", 
                        color="gray.300", 
                        letter_spacing="0.08em",
                        max_width="600px",
                        text_align="center"
                    ),
                    initial={"opacity": 0, "y": 20},
                    animate={"opacity": 1, "y": 0},
                    transition={"duration": 0.8, "delay": 0.4}
                ),

                motion_div(
                    rx.hstack(
                        rx.button(
                            "Explore Creations 🚀", 
                            size="3", 
                            variant="solid",
                            color_scheme="cyan",
                            border_radius="12px",
                            cursor="pointer",
                            padding="1.5rem 2rem",
                            font_weight='bold'
                        ),
                        rx.button(
                            "Get in Touch 💬", 
                            size="3", 
                            variant="outline",
                            color_scheme="gray",
                            border_radius="12px",
                            cursor="pointer",
                            padding="1.5rem 2rem"
                        ),
                        spacing="4",
                        margin_top="1.5rem"
                    ),
                    initial={"opacity": 0, "y": 20},
                    animate={"opacity": 1, "y": 0},
                    transition={"duration": 0.8, "delay": 0.6}
                ),
                
                align_items="center",
                text_align="center",
                z_index="5",
                position="relative",
                spacing="3"
            ),
            height="100vh",
            width="100vw",
            padding="0 5%"
        ),

        # Features Section
        rx.vstack(
            rx.vstack(
                rx.text("CAPABILITIES", color="#00d9ff", weight='bold', letter_spacing="0.2em", font_size="0.85rem"),
                rx.heading("Crafting Digital Brilliance", size="8", color="gray", weight='bold'),
                rx.text("Combining high-performance frontend architectures with cutting-edge visual design.", color="gray.400", max_width="600px", text_align="center"),
                align_items="center",
                margin_bottom="3rem"
            ),
            rx.grid(
                feature_card("🔮", "3D Interactive Worlds", "Seamlessly blending WebGL and Spline canvas layers into fluid reactive user experiences."),
                feature_card("⚡", "High-Performance Code", "Engineered with modern reactive architectures running at smooth 60fps frame rates."),
                feature_card("🎨", "Cyber & Neomorphic UI", "Custom dark modes, vibrant HSL gradients, glassmorphism, and dynamic lighting."),
                feature_card("🚀", "AI & Motion Synergy", "Integrating fluid physics, Framer Motion transitions, and smart algorithmic logic."),
                columns=rx.breakpoints(initial="1", md="2", lg="4"),
                spacing="6",
                width="100%"
            ),
            padding="6rem 8%",
            position="relative",
            z_index="5",
            id="features"
        ),

        # Metrics Bar
        rx.hstack(
            stats_badge("Frame Rate", "60 FPS"),
            stats_badge("Aesthetic Precision", "100%"),
            stats_badge("3D & Motion Layers", "Spline / Framer"),
            stats_badge("User Experience", "Ultra-Fluid"),
            width="84%",
            margin="0 auto",
            justify="between",
            wrap="wrap",
            gap="1rem",
            position="relative",
            z_index="5",
            padding="2rem 0"
        ),

        # Selected Work Section
        rx.vstack(
            rx.vstack(
                rx.text("PORTFOLIO", color="#ff006e", weight='bold', letter_spacing="0.2em", font_size="0.85rem"),
                rx.heading("Selected Works", size="8", color="gray", weight='bold'),
                rx.text("A spotlight on interactive projects and experimental web apps.", color="gray.400"),
                align_items="center",
                margin_bottom="3rem"
            ),
            rx.grid(
                project_card("Spline Metaverse Portal", "3D WebGL", "Interactive 3D landing page featuring real-time light physics and spatial audio.", ["Spline", "Reflex", "Python"]),
                project_card("CyberPulse Dashboard", "Analytics UI", "Futuristic real-time analytics suite with glassmorphism telemetry widgets.", ["React", "Framer", "CSS3"]),
                project_card("Aether Sound Visualizer", "Audio Reactive", "Canvas-driven sound wave visualizer responding dynamically to ambient audio.", ["WebAudio", "Canvas", "JS"]),
                columns=rx.breakpoints(initial="1", md="3"),
                spacing="6",
                width="100%"
            ),
            padding="6rem 8%",
            position="relative",
            z_index="5",
            id="work"
        ),

        # Contact Section
        rx.center(
            rx.vstack(
                rx.heading("Let's Build Something Extraordinary", size="7", color="gray", text_align="center"),
                rx.text("Have an ambitious idea or want to collaborate? Reach out today.", color="gray.400", text_align="center", max_width="500px"),
                motion_div(
                    rx.button(
                        "Start a Conversation ✨", 
                        size="3", 
                        background="linear-gradient(135deg, #00d9ff, #ff006e)",
                        color="gray",
                        font_weight='bold',
                        padding="1.5rem 2.5rem",
                        border_radius="12px",
                        box_shadow="0 0 25px rgba(0, 217, 255, 0.4)",
                        cursor="pointer"
                    ),
                    whileHover={"scale": 1.05},
                    whileTap={"scale": 0.95},
                    margin_top="1.5rem"
                ),
                align_items="center",
                padding="5rem 2rem",
                background="rgba(255, 255, 255, 0.02)",
                border="1px solid rgba(255, 255, 255, 0.08)",
                border_radius="24px",
                backdrop_filter="blur(16px)",
                width="100%",
                max_width="900px"
            ),
            padding="4rem 8% 8rem",
            position="relative",
            z_index="5",
            id="contact"
        ),

        # Footer
        rx.hstack(
            rx.text("© 2026 Jokku. All rights reserved.", color="gray.500", font_size="0.85rem"),
            rx.spacer(),
            rx.text("Built with Reflex, Framer Motion & Spline 3D", color="gray.500", font_size="0.85rem"),
            width="100%",
            padding="2rem 8%",
            border_top="1px solid rgba(255, 255, 255, 0.05)",
            position="relative",
            z_index="5"
        ),

        background="#050505",
        position="relative",
        overflow_x="hidden",
        width="100vw",
        min_height="100vh",
        font_family="Inter, sans-serif"
    )


# ==========================================
# 4. REFLEX APP INITIALIZATION
# ==========================================

app = rx.App(
    style={
        "background": "#050505",
        "color": "gray"
    }
)
app.add_page(index, title="Jokku — Futuristic Animated World")