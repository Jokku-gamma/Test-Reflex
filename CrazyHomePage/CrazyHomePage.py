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

def floating_hud_card(title: str, subtitle: str, top: str, left: str, delay: float, y_offset: int):
    """Creates a glassmorphic card that floats continuously."""
    return motion_div(
        rx.vstack(
            rx.text(title, color="white", weight="bold", size="4"),
            rx.text(subtitle, color="gray.400", size="2"),
            rx.box(width="30px", height="2px", background="linear-gradient(90deg, #00f2fe, #4facfe)", border_radius="2px", margin_top="0.5em"),
            background="rgba(255, 255, 255, 0.03)",
            backdrop_filter="blur(16px)",
            border="1px solid rgba(255, 255, 255, 0.05)",
            padding="1.5em",
            border_radius="16px",
            box_shadow="0 10px 40px rgba(0, 0, 0, 0.3)",
        ),
        position="absolute", top=top, left=left, z_index="4",
        initial={"opacity": 0, "scale": 0.8},
        # Fades in, then floats up and down infinitely
        animate={"opacity": 1, "scale": 1, "y": [0, y_offset, 0]},
        transition={
            "opacity": {"duration": 1, "delay": delay},
            "scale": {"duration": 1, "delay": delay, "ease": "backOut"},
            "y": {"duration": 5, "repeat": 999, "ease": "easeInOut", "delay": delay}
        },
        whileHover={"scale": 1.1, "border": "1px solid rgba(0, 242, 254, 0.4)"}
    )


# ==========================================
# 3. CINEMATIC WELCOME PAGE
# ==========================================

def index():
    return rx.box(
        # 1. Background Orbs
        glowing_orb("#4facfe", top="-10%", left="10%", delay=0),
        glowing_orb("#f093fb", top="50%", left="60%", delay=2),
        glowing_orb("#43e97b", top="60%", left="0%", delay=4),
        
        # 2. 3D Scene Layer
        rx.box(
            spline(scene="https://prod.spline.design/joLpOOYbGL-10EJ4/scene.splinecode"),
            position="absolute", top="0", left="0", width="100%", height="100%", z_index="1",
            opacity="0.8" 
        ),
        
        # 3. Floating HUD Elements (Graphics moving around)
        floating_hud_card("Telemetry", "Live Datastream", top="20%", left="15%", delay=0.5, y_offset=-20),
        floating_hud_card("Neural Net", "Weights Optimized", top="65%", left="12%", delay=0.7, y_offset=25),
        floating_hud_card("Hardware I/O", "Synchronized", top="25%", left="75%", delay=0.9, y_offset=-15),
        floating_hud_card("EKF Mapping", "Sensors Calibrated", top="70%", left="70%", delay=1.1, y_offset=20),
        
        # 4. Center Hero Typography
        rx.center(
            rx.vstack(
                motion_div(
                    rx.text(
                        "SYSTEM.ONLINE", 
                        size="3", weight="bold", letter_spacing="0.5em", 
                        color="#00f2fe"
                    ),
                    initial={"opacity": 0, "y": -20},
                    animate={"opacity": 1, "y": 0},
                    transition={"duration": 1, "ease": "easeOut"}
                ),
                
                motion_div(
                    rx.heading(
                        "NEURAL", weight="bold",
                        style={
                            "background": "linear-gradient(180deg, #ffffff 0%, #a1a1aa 100%)",
                            "-webkit-background-clip": "text",
                            "-webkit-text-fill-color": "transparent",
                            "font-size": "min(8vw, 8rem)",
                            "line-height": "1"
                        }
                    ),
                    initial={"opacity": 0, "scale": 0.9},
                    animate={"opacity": 1, "scale": 1},
                    transition={"duration": 1.2, "delay": 0.2, "ease": [0.16, 1, 0.3, 1]}
                ),
                
                motion_div(
                    rx.heading(
                        "ARCHITECTURE", weight="bold",
                        style={
                            "background": "linear-gradient(90deg, #00f2fe 0%, #4facfe 100%)",
                            "-webkit-background-clip": "text",
                            "-webkit-text-fill-color": "transparent",
                            "font-size": "min(8vw, 8rem)",
                            "line-height": "1"
                        }
                    ),
                    initial={"opacity": 0, "scale": 0.9},
                    animate={"opacity": 1, "scale": 1},
                    transition={"duration": 1.2, "delay": 0.3, "ease": [0.16, 1, 0.3, 1]}
                ),
                
                motion_div(
                    rx.button(
                        "INITIALIZE SEQUENCE", 
                        size="4", 
                        style={
                            "background": "rgba(0, 242, 254, 0.05)",
                            "backdropFilter": "blur(5px)",
                            "border": "1px solid #00f2fe",
                            "boxShadow": "0 0 20px rgba(0, 242, 254, 0.2)",
                            "borderRadius": "4px",
                            "padding": "1.8em 4em",
                            "color": "#00f2fe",
                            "cursor": "pointer",
                            "letterSpacing": "0.15em",
                            "marginTop": "2em",
                        }
                    ),
                    initial={"opacity": 0, "y": 30},
                    animate={"opacity": 1, "y": 0},
                    transition={"duration": 1, "delay": 0.6},
                    whileHover={
                        "scale": 1.05, 
                        "backgroundColor": "rgba(0, 242, 254, 0.2)",
                        "boxShadow": "0 0 40px rgba(0, 242, 254, 0.6)"
                    },
                    whileTap={"scale": 0.95}
                ),
                
                align_items="center",
                justify_content="center",
                z_index="5",
                position="relative"
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