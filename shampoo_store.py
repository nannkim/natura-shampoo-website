import streamlit as st
import pandas as pd
import time

# ============================================================================
# PAGE CONFIGURATION (Apple-style)
# ============================================================================
st.set_page_config(
    page_title="Natura | Premium Organic Shampoo",
    page_icon="🧴",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# APPLE-STYLE CSS
# ============================================================================
def apply_apple_design():
    st.markdown("""
    <style>
    /* Apple-style minimalism */
    .main {
        background-color: #ffffff;
        padding: 0;
    }
    
    .block-container {
        padding-top: 2rem;
        padding-bottom: 0;
    }
    
    /* Apple typography */
    .apple-header {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-weight: 700;
        color: #1d1d1f;
        text-align: center;
        margin-bottom: 0.5rem;
        font-size: 3.5rem;
    }
    
    .apple-subheader {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-weight: 400;
        color: #86868b;
        text-align: center;
        font-size: 1.8rem;
        margin-bottom: 3rem;
    }
    
    /* Hero section */
    .hero-section {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 8rem 2rem;
        text-align: center;
        border-radius: 0 0 30px 30px;
        margin: -2rem -1rem 4rem -1rem;
    }
    
    /* Product cards */
    .product-card {
        background: #ffffff;
        border-radius: 18px;
        padding: 2.5rem;
        margin: 1rem 0;
        border: 1px solid #f0f0f0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .product-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.12);
    }
    
    /* Apple-style buttons */
    .stButton > button {
        background: #0071e3;
        color: white;
        border: none;
        padding: 0.9rem 2.5rem;
        border-radius: 12px;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-weight: 500;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        background: #0077ed;
        transform: scale(1.03);
        box-shadow: 0 8px 20px rgba(0,113,227,0.3);
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Feature tags */
    .feature-tag {
        background: #f5f5f7;
        color: #515154;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        margin: 0.3rem;
        display: inline-block;
    }
    </style>
    """, unsafe_allow_html=True)

# ============================================================================
# PRODUCT DATA
# ============================================================================
def get_products():
    return [
        {
            "id": 1,
            "name": "Natura Organic Shampoo",
            "description": "Crafted with 100% organic ingredients for hair that radiates health and vitality. Gentle enough for daily use.",
            "price": 29.99,
            "features": ["100% Organic", "Cruelty Free", "Vegan", "Eco Packaging"],
            "ingredients": "Organic Aloe Vera, Coconut Oil, Argan Oil, Essential Oils",
            "benefits": "Deep Hydration • Scalp Health • Natural Shine • Daily Use"
        },
        {
            "id": 2,
            "name": "Natura Volume Boost", 
            "description": "Lightweight formula that adds body and bounce without weighing hair down. For fine or flat hair.",
            "price": 32.99,
            "features": ["Volume Boost", "Lightweight", "Sulfate Free", "Color Safe"],
            "ingredients": "Bamboo Extract, Biotin, Rosemary Oil, Vitamin B5",
            "benefits": "Fuller Hair • Long-Lasting Volume • Strength • Body"
        },
        {
            "id": 3,
            "name": "Natura Scalp Therapy",
            "description": "Soothes and balances the scalp while promoting healthy hair growth. For sensitive or irritated scalp.",
            "price": 34.99,
            "features": ["Scalp Care", "Dandruff Control", "pH Balanced", "Therapeutic"],
            "ingredients": "Tea Tree Oil, Salicylic Acid, Peppermint, Chamomile",
            "benefits": "Soothed Scalp • Reduced Irritation • Healthy Growth • Balance"
        }
    ]

# ============================================================================
# SESSION STATE MANAGEMENT
# ============================================================================
def initialize_session():
    if 'cart' not in st.session_state:
        st.session_state.cart = []
    if 'view' not in st.session_state:
        st.session_state.view = "home"

# ============================================================================
# HERO SECTION
# ============================================================================
def show_hero():
    st.markdown("""
    <div class="hero-section">
        <h1 class="apple-header">Natura</h1>
        <p class="apple-subheader">Organic Shampoo. Radical Results.</p>
        <p style="font-size: 1.3rem; color: #515154; max-width: 600px; margin: 0 auto; line-height: 1.6;">
            Formulated with nature's finest ingredients. Transforming hair care through purity, performance, and sustainable practices.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PRODUCTS SECTION
# ============================================================================
def show_products():
    st.markdown('<h2 class="apple-header" style="font-size: 2.5rem;">The Natura Collection</h2>', unsafe_allow_html=True)
    st.markdown('<p class="apple-subheader" style="font-size: 1.3rem;">Three extraordinary formulas. One perfect choice.</p>', unsafe_allow_html=True)
    
    products = get_products()
    
    # Create three columns for products
    col1, col2, col3 = st.columns(3)
    
    with col1:
        product = products[0]
        show_product_card(product)
    
    with col2:
        product = products[1]
        show_product_card(product)
    
    with col3:
        product = products[2]
        show_product_card(product)

def show_product_card(product):
    st.markdown(f"""
    <div class="product-card">
        <h3 style="color: #1d1d1f; font-size: 1.8rem; margin-bottom: 1rem;">{product['name']}</h3>
        <p style="color: #86868b; font-size: 1rem; line-height: 1.6; margin-bottom: 1.5rem;">{product['description']}</p>
        <h4 style="color: #1d1d1f; font-size: 2.2rem; margin-bottom: 1.5rem;">${product['price']}</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Features
    features_html = "".join([f"<span class='feature-tag'>{feature}</span>" for feature in product['features']])
    st.markdown(f"<div style='text-align: center; margin: 1.5rem 0;'>{features_html}</div>", unsafe_allow_html=True)
    
    # Benefits
    st.markdown(f"<p style='text-align: center; color: #515154; font-size: 0.95rem; line-height: 1.5; margin: 1.5rem 0;'>{product['benefits']}</p>", unsafe_allow_html=True)
    
    # Add to cart button
    if st.button(f"Add to Cart · ${product['price']}", key=f"add_{product['id']}"):
        st.session_state.cart.append(product)
        st.success(f"✅ Added {product['name']} to cart!")
        time.sleep(1)
        st.rerun()
    
    # Learn more button
    if st.button("Learn More", key=f"learn_{product['id']}", type="secondary"):
        st.session_state.view = f"product_{product['id']}"
        st.session_state.current_product = product
        st.rerun()

# ============================================================================
# CART SIDEBAR
# ============================================================================
def show_cart_sidebar():
    with st.sidebar:
        st.markdown("<h2 style='color: #1d1d1f; font-family: -apple-system;'>🛒 Your Cart</h2>", unsafe_allow_html=True)
        
        if not st.session_state.cart:
            st.markdown("<p style='color: #86868b;'>Your cart is empty</p>", unsafe_allow_html=True)
        else:
            # Show cart items
            total = 0
            for item in st.session_state.cart:
                st.markdown(f"""
                <div style='border-bottom: 1px solid #f0f0f0; padding: 0.8rem 0;'>
                    <strong>{item['name']}</strong><br>
                    <span style='color: #86868b;'>${item['price']}</span>
                </div>
                """, unsafe_allow_html=True)
                total += item['price']
            
            st.markdown(f"<h3 style='color: #1d1d1f; border-top: 1px solid #f0f0f0; padding-top: 1rem;'>Total: ${total:.2f}</h3>", unsafe_allow_html=True)
            
            # Checkout button
            if st.button("Proceed to Checkout", type="primary", use_container_width=True):
                st.balloons()
                st.success("🚀 Checkout system would be integrated here with Stripe!")
            
            # Clear cart button
            if st.button("Clear Cart", type="secondary", use_container_width=True):
                st.session_state.cart = []
                st.rerun()

# ============================================================================
# FOOTER
# ============================================================================
def show_footer():
    st.markdown("""
    <div style='background: #f5f5f7; padding: 4rem 2rem; margin-top: 6rem; border-radius: 30px 30px 0 0;'>
        <div style='max-width: 1000px; margin: 0 auto;'>
            <div style='display: grid; grid-template-columns: repeat(4, 1fr); gap: 3rem;'>
                <div>
                    <h4 style='color: #1d1d1f; font-family: -apple-system;'>Natura</h4>
                    <p style='color: #86868b; line-height: 1.6;'>Premium organic hair care that makes a difference for you and the planet.</p>
                </div>
                <div>
                    <h4 style='color: #1d1d1f; font-family: -apple-system;'>Shop</h4>
                    <p style='color: #86868b; line-height: 1.6;'>All Products<br>Best Sellers<br>New Arrivals<br>Gift Sets</p>
                </div>
                <div>
                    <h4 style='color: #1d1d1f; font-family: -apple-system;'>Support</h4>
                    <p style='color: #86868b; line-height: 1.6;'>Contact Us<br>Shipping & Returns<br>FAQ<br>Track Order</p>
                </div>
                <div>
                    <h4 style='color: #1d1d1f; font-family: -apple-system;'>About</h4>
                    <p style='color: #86868b; line-height: 1.6;'>Our Story<br>Sustainability<br>Ingredients<br>Press</p>
                </div>
            </div>
            <div style='text-align: center; margin-top: 4rem; color: #86868b; border-top: 1px solid #e0e0e0; padding-top: 2rem;'>
                <p>© 2024 Natura Organic. All rights reserved. | Privacy Policy | Terms of Use</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# MAIN APP
# ============================================================================
def main():
    # Apply Apple design
    apply_apple_design()
    
    # Initialize session state
    initialize_session()
    
    # Show cart sidebar
    show_cart_sidebar()
    
    # Show main content based on current view
    if st.session_state.view == "home":
        show_hero()
        show_products()
    
    # Show footer on all pages
    show_footer()

if __name__ == "__main__":
    main()
