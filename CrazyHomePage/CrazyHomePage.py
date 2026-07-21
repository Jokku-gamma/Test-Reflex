import reflex as rx
from reflex.components.component import NoSSRComponent

# ==========================================
# 1. REACT WRAPPERS
# ==========================================

class SplineScene(NoSSRComponent):
    library = "@splinetool/react-spline"
    lib_dependencies = ["@splinetool/runtime"]
    tag = "Spline"
    is_default = True
    scene: rx.Var[str]

spline = SplineScene.create

class MotionDiv(rx.Component):
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
# 2. ANIMATION HELPERS
# ==========================================

def glowing_orb(color: str, top: str, left: str, delay: float):
    """Creates a massive blurred background sphere that pulses infinitely."""
    return motion_div(
        rx.box(
            width="40vw", height="40vw",
            background=color,
            border_radius="50%",
            filter="blur(150px)",
            opacity="0.3",
        ),
        position="absolute", top=top, left=left, z_index="0",
        initial={"scale": 0.8, "opacity": 0.1},
        animate={"scale": [0.8, 1.2, 0.8], "opacity": [0.1, 0.4, 0.1]},
        transition={"duration": 8, "repeat": 999, "delay": delay, "ease": "easeInOut"}
    )

def feature_card(icon: str, title: str, description: str):
    """Creates an animated feature card."""
    return motion_div(
        rx.vstack(
            rx.text(icon, size="6"),
            rx.text(title, weight="bold", size="4", color="white"),
            rx.text(description, color="gray.400", size="2"),
            background="rgba(255, 255, 255, 0.03)",
            backdrop_filter="blur(10px)",
            border="1px solid rgba(79, 184, 255, 0.2)",
            padding="2em",
            border_radius="12px",
            spacing="2",
        ),
        initial={"opacity": 0, "y": 20},
        animate={"opacity": 1, "y": 0},
        transition={"duration": 0.8},
        whileHover={"scale": 1.05, "borderColor": "rgba(79, 184, 255, 0.5)"}
    )


# ==========================================
# 3. PERSONAL WELCOME PAGE
# ==========================================

def index():
    """Personal welcome page for Jokku."""
    return rx.box(
        # Background Orbs with animations
        glowing_orb("#4fb8ff", top="-20%", left="10%", delay=0),
        glowing_orb("#ff006e", top="40%", left="70%", delay=2),
        glowing_orb("#00d9ff", top="70%", left="5%", delay=4),
        
        # 3D Scene Layer
        rx.box(
            spline(scene="https://prod.spline.design/joLpOOYbGL-10EJ4/scene.splinecode"),
            position="absolute", top="0", left="0", width="100%", height="100%", z_index="1",
            opacity="0.7"
        ),
        
        # Center Welcome Message
        rx.center(
            motion_div(
                rx.heading(
                    "Welcome jokku",
                    weight="bold",
                    style={
                        "font-size": "min(10vw, 6rem)",
                        "background": "linear-gradient(135deg, #4fb8ff 0%, #00d9ff 50%, #ff006e 100%)",
                        "-webkit-background-clip": "text",
                        "-webkit-text-fill-color": "transparent",
                        "line-height": "1",
                        "letter-spacing": "0.05em"
                    }
                ),
                initial={"opacity": 0, "scale": 0.8},
                animate={"opacity": 1, "scale": 1},
                transition={"duration": 1.2, "ease": [0.16, 1, 0.3, 1]}
            ),
            height="100vh",
            width="100vw"
        ),
        
        background="#050505",
        position="relative",
        overflow="hidden",
        height="100vh",
        width="100vw",
        font_family="Inter, sans-serif"
    )

app = rx.App()
app.add_page(index)