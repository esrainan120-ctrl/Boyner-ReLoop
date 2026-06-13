import streamlit as st
st.image("images/boyner_logo.png", width=220)
st.markdown(
    '<div class="main-title">ReLoop Digital Product Passport</div>',
    unsafe_allow_html=True
)

st.markdown("""
<style>
html, body, [class*="css"] {
    color: #1C2440 !important;
}

.stApp {
    background-color: #F7F8FA;
    color: #1C2440;
}

p, span, div, h1, h2, h3, h4, h5 {
    color: #1C2440;
}

.product-card {
    text-align: center;
    font-weight: 700;
    color: #1C2440 !important;
}

.metric-value {
    color: #0b6b2b !important;
    font-size: 34px;
    font-weight: 700;
}
.stApp {
    background-color: #F7F8FA;
}

.main-title {
    font-size: 48px;
    font-weight: 800;
    color: #1C2440;
}

.green-box {
    background: linear-gradient(90deg,#E8F7EF,#DFF5E7);
    border-left: 6px solid #27AE60;
    padding: 18px;
    border-radius: 16px;
    color: #1C2440;
}

.metric-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.05);
    text-align:center;
}

.passport-card {
    background:white;
    border-radius:20px;
    padding:20px;
    box-shadow:0px 4px 20px rgba(0,0,0,0.05);
}

.fabric-card {
    background:#F5F8FF;
    border-radius:16px;
    padding:15px;
    text-align:center;
}
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
        "water": 10000,
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
        "water": 2700,
        "co2": 5,
        "image": "images/tisort.png"
    }
}
fabric_impact = {
    "Pamuk": {
        "water_text": "%99'a kadar su tasarrufu",
        "co2_text": "%93'e kadar karbon emisyonu azaltımı",
        "energy_text": "Sıfır pamuk üretimine kıyasla tarımsal kaynak kullanımını azaltır."
    },
    "Denim": {
        "water_text": "Pantolon başına yaklaşık 5.500 litre su tasarrufu",
        "co2_text": "%61'e kadar karbon emisyonu azaltımı",
        "energy_text": "Atık denimlerin kullanım ömrünü uzatarak yeni kumaş ihtiyacını azaltır."
    },
    "Polyester": {
        "water_text": "%68–90 arasında su tasarrufu",
        "co2_text": "%75'e kadar karbon emisyonu azaltımı",
        "energy_text": "%59–70 oranında enerji tasarrufu"
    },
    "Naylon / Poliamid": {
        "water_text": "%54–58 arasında su tasarrufu",
        "co2_text": "Petrol türevli ham madde kullanımını azaltır.",
        "energy_text": "Yüksek performanslı atık kumaşların yeniden kullanımını destekler."
    },
    "Viskoz": {
        "water_text": "%50 daha az su kullanımı",
        "co2_text": "%50 daha az emisyon",
        "energy_text": "Kapalı döngü üretim mantığıyla kimyasal ve endüstriyel israfı azaltır."
    }
}

bags = {
    "BAG001": {
        "name": "ReLoop Denim Çanta",
        "description": "Denim pantolon ve denim gömlekten ileri dönüştürüldü.",
        "items": ["denim_pantolon", "denim_gomlek"],
        "conversion_rate": 0.25,
        "output_image": "images/denim_canta.png",
        "fabric_mix": {
            "Pamuk": 95,
            "Polyester": 5
        },
        "main_material": "Denim",
        "passport": {
            "Ürün Kodu": "BAG001",
            "Dönüşüm Türü": "İleri dönüşüm / Upcycling",
            "Malzeme Türü": "Denim ağırlıklı karışım",
            "Üretim Modeli": "Parça kumaş tekniği",
            "Üretici": "Kadın kooperatifi üretimi"
        }
    },

    "BAG002": {
        "name": "ReLoop Bez Çanta",
        "description": "Pamuklu gömlek ve tişörtten ileri dönüştürüldü.",
        "items": ["pamuklu_gomlek", "tisort"],
        "conversion_rate": 0.25,
        "output_image": "images/bez_canta.png",
        "fabric_mix": {
            "Pamuk": 90,
            "Polyester": 10
        },
        "main_material": "Pamuk",
        "passport": {
            "Ürün Kodu": "BAG002",
            "Dönüşüm Türü": "İleri dönüşüm / Upcycling",
            "Malzeme Türü": "Pamuk ağırlıklı karışım",
            "Üretim Modeli": "Parça kumaş tekniği",
            "Üretici": "Kadın kooperatifi üretimi"
        }
    }
}

query_params = st.query_params
bag_id = query_params.get("id", "BAG001")

st.markdown('<div class="main-title">Boyner ReLoop ♻️</div>', unsafe_allow_html=True)
st.subheader("Dijital Ürün Pasaportu")
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

st.subheader("Malzeme Şeffaflığı")

mix_cols = st.columns(len(bag["fabric_mix"]))


for i, (fabric, percentage) in enumerate(bag["fabric_mix"].items()):
            with mix_cols[i]:
                st.markdown(
                    f"""
                    <div class="fabric-card">
                        <h4>{fabric}</h4>
                        <h2>%{percentage}</h2>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

st.write("Bu çantanın tahmini kumaş içeriği, kullanılan kaynak ürünlerin türüne göre hesaplanmıştır.")

st.subheader("Kumaş Türüne Göre Ekosistem Katkısı")

main_material = bag["main_material"]

if main_material in fabric_impact:
    impact = fabric_impact[main_material]
    st.success(f"{main_material} ağırlıklı bu ürün için temel ekosistem katkısı:")
    st.write("💧", impact["water_text"])
    st.write("☁️", impact["co2_text"])
    st.write("⚡", impact["energy_text"])

for fabric, percentage in bag["fabric_mix"].items():
    if fabric in fabric_impact:
        impact = fabric_impact[fabric]

        with st.expander(f"{fabric} - Çanta içeriğinin %{percentage}'i"):
            st.write("💧", impact["water_text"])
            st.write("☁️", impact["co2_text"])
            st.write("⚡", impact["energy_text"])

st.subheader("Döngüsel Dönüşüm Yolculuğu")
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

st.subheader("Dijital Ürün Pasaportu")

st.markdown('<div class="passport-card">', unsafe_allow_html=True)

for key, value in bag["passport"].items():
    st.write(f"**{key}:** {value}")

st.markdown('</div>', unsafe_allow_html=True)

st.divider()

st.markdown(
    '<div class="green-box">🌱 Döngüsel modaya katkın için teşekkür ederiz!<br>Sürdürülebilir bir gelecek için birlikte dönüşüyoruz.</div>',
    unsafe_allow_html=True
)
