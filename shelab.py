import streamlit as st

st.set_page_config(page_title="Boyner ReLoop", page_icon="♻️", layout="wide")

st.markdown("""
<style>
.main-title {
    font-size: 46px;
    font-weight: 800;
}
.green-box {
    background-color: #e7f6ec;
    padding: 18px;
    border-radius: 12px;
    color: #0b6b2b;
    font-size: 18px;
}
.info-box {
    background-color: #eaf3ff;
    padding: 14px;
    border-radius: 12px;
    color: #164b8f;
}
.metric-value {
    color: #0b6b2b;
    font-size: 34px;
    font-weight: 700;
}
.product-card {
    text-align: center;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

impact_data = {
    "denim_pantolon": {
        "name": "Denim Pantolon",
        "water": 8000,
        "co2": 20,
        "image": "images/denim_pantolon.png"
    },
    "denim_gomlek": {
        "name": "Denim Gömlek",
        "water": 3000,
        "co2": 7,
        "image": "images/denim_gomlek.png"
    },
    "pamuklu_gomlek": {
        "name": "Pamuklu Gömlek",
        "water": 2700,
        "co2": 6,
        "image": "images/pamuklu_gomlek.png"
    },
    "tisort": {
        "name": "Pamuklu Tişört",
        "water": 2500,
        "co2": 5,
        "image": "images/tisort.png"
    }
}

bags = {
    "BAG001": {
        "name": "ReLoop Denim Çanta",
        "description": "Denim pantolon ve denim gömlekten ileri dönüştürüldü.",
        "items": ["denim_pantolon", "denim_gomlek"],
        "conversion_rate": 0.25,
        "output_image": "images/denim_canta.png"
    },
    "BAG002": {
        "name": "ReLoop Bez Çanta",
        "description": "Pamuklu gömlek ve tişörtten ileri dönüştürüldü.",
        "items": ["pamuklu_gomlek", "tisort"],
        "conversion_rate": 0.25,
        "output_image": "images/bez_canta.png"
    }
}

query_params = st.query_params
bag_id = query_params.get("id", "BAG001")

st.markdown('<div class="main-title">Boyner ReLoop ♻️</div>', unsafe_allow_html=True)
st.subheader("Çantanın Dönüşüm Hikayesi")
st.write(f"Okutulan QR: **{bag_id}**")

if bag_id not in bags:
    st.error("Bu QR koda ait çanta kaydı bulunamadı.")
    st.stop()

bag = bags[bag_id]

total_water = sum(impact_data[item]["water"] for item in bag["items"])
total_co2 = sum(impact_data[item]["co2"] for item in bag["items"])

saved_water = total_water * bag["conversion_rate"]
saved_co2 = total_co2 * bag["conversion_rate"]

st.markdown('<div class="green-box">✅ Bu çanta Boyner ReLoop sistemiyle üretildi.</div>', unsafe_allow_html=True)

st.divider()

st.header(bag["name"])
st.write(bag["description"])

col1, col2, col3 = st.columns(3)

with col1:
    st.write("💧 Su Tasarrufu")
    st.markdown(f'<div class="metric-value">{saved_water:,.0f} litre</div>', unsafe_allow_html=True)

with col2:
    st.write("☁️ CO₂ Katkısı")
    st.markdown(f'<div class="metric-value">{saved_co2:.1f} kg</div>', unsafe_allow_html=True)

with col3:
    st.write("🌿 Yeniden Değerlendirilen Ürün")
    st.markdown(f'<div class="metric-value">{len(bag["items"])} adet</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="info-box">ℹ️ Bu değerler, ürün bazlı tahmini su tüketimi ve karbon ayak izi katsayıları üzerinden hesaplanmaktadır.</div>',
    unsafe_allow_html=True
)

st.subheader("Ürünün Yolculuğu")
st.write("Bu çantanın üretiminde kullanılan ürünler:")

c1, plus_col, c2, arrow_col, c3 = st.columns([2, 0.5, 2, 0.5, 2])

item1 = impact_data[bag["items"][0]]
item2 = impact_data[bag["items"][1]]

with c1:
    st.image(item1["image"], use_container_width=True)
    st.markdown(f"<div class='product-card'>{item1['name']}</div>", unsafe_allow_html=True)

with plus_col:
    st.markdown("<h1 style='text-align:center; margin-top:90px;'>+</h1>", unsafe_allow_html=True)

with c2:
    st.image(item2["image"], use_container_width=True)
    st.markdown(f"<div class='product-card'>{item2['name']}</div>", unsafe_allow_html=True)

with arrow_col:
    st.markdown("<h1 style='text-align:center; margin-top:90px;'>→</h1>", unsafe_allow_html=True)

with c3:
    st.image(bag["output_image"], use_container_width=True)
    st.markdown(f"<div class='product-card'>{bag['name']}</div>", unsafe_allow_html=True)

st.divider()

st.markdown(
    '<div class="green-box">🌱 Döngüsel modaya katkın için teşekkür ederiz!<br>Sürdürülebilir bir gelecek için birlikte dönüşüyoruz.</div>',
    unsafe_allow_html=True
)
