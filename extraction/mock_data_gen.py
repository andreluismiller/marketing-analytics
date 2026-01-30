import json
import random
import os
from datetime import datetime, timedelta
from faker import Faker

fake = Faker('pt_BR')

DATE_START = datetime(2024, 11, 15)
DAYS = 11
OUTPUT_DIR = "mock_respostas_api"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)


# Funções para gerar dados teste de ads por API em período de 10 dias

def generate_google_ads_response(date, camp_id):
    # Google Ads API response típica
    spend = round(random.uniform(100, 1000), 2)
    clicks = random.randint(50, 200)
    return {
        "customer": {"id": "123456", "descriptiveName": "Cliente Teste"},
        "campaign": {"id": camp_id, "name": f"GAds_Camp_{camp_id}", "advertisingChannelType": "SEARCH"},
        "adGroup": {"id": f"ag_{camp_id}", "name": "Conjunto_Teste"},
        "adGroupAd": {"ad": {"id": f"ad_{camp_id}", "type": "TEXT_AD"}},
        "metrics": {"costMicros": int(spend * 1000000), "clicks": str(clicks), "impressions": str(clicks*20)},
        "segments": {"date": date.strftime('%Y-%m-%d')}
    }

def generate_meta_ads_response(date, camp_id):
    # Meta Marketing API response típica
    spend = round(random.uniform(50, 500), 2)
    return {
        "campaign_id": camp_id,
        "campaign_name": f"Meta_Camp_{camp_id}",
        "date_start": date.strftime('%Y-%m-%d'),
        "spend": str(spend),
        "clicks": str(random.randint(20, 150)),
        "actions": [{"action_type": "purchase", "value": str(random.randint(0, 5))}]
    }

def generate_tiktok_ads_response(date, camp_id):
    # TikTok Marketing API response típica
    return {
        "campaign_id": camp_id,
        "campaign_name": f"TikTok_Camp_{camp_id}",
        "stat_time_day": date.strftime('%Y-%m-%d'),
        "metrics": {"spend": str(round(random.uniform(30, 200), 2)), "clicks": str(random.randint(100, 500))}
    }

def generate_x_ads_response(date, camp_id):
    # X Business API response típica
    spend = round(random.uniform(10, 100), 2)
    return {
        "campaign_id": camp_id,
        "date": date.strftime('%Y-%m-%d'),
        "metrics": {"billed_charge_local_micro": int(spend * 1000000), "impressions": random.randint(500, 2000)}
    }

# --- MAPEAMENTO DE PLATAFORMAS E CHAVES DE RESPOSTA ---
platforms = {
    "google": {"func": generate_google_ads_response, "root_key": "results"},
    "meta": {"func": generate_meta_ads_response, "root_key": "data"},
    "tiktok": {"func": generate_tiktok_ads_response, "root_key": "data"},
    "x": {"func": generate_x_ads_response, "root_key": "data"}
}

print(f"Gerando respostas de API em: {os.path.abspath(OUTPUT_DIR)}")

for plat_name, config in platforms.items():
    filename = os.path.join(OUTPUT_DIR, f"api_response_{plat_name}.json")
    
    # Lista para todos os registros das APIs
    api_payload = []
    
    for i in range(DAYS):
        current_date = DATE_START + timedelta(days=i)
        for c_id in ["99901", "99902"]:
            record = config["func"](current_date, c_id)
            api_payload.append(record)
    
    # Monta o objeto final simulando metadados das APIs
    final_response = {
        config["root_key"]: api_payload,
        "metadata": {
            "total_count": len(api_payload),
            "period": "2024-11-15 to 2024-11-25"
        }
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(final_response, f, ensure_ascii=False, indent=4)
    
    print(f" ✔️ {plat_name.upper()}: JSON fiel gerado em {filename}")

print("\nSucesso! Os arquivos agora são objetos JSON únicos com listas internas.")