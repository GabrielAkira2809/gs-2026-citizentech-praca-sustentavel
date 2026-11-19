
import csv, json
from pathlib import Path
BASE = Path(__file__).resolve().parent

def consumo_kwh(unidades, potencia_w, horas_dia, dias):
    return unidades * potencia_w * horas_dia * dias / 1000

def calcular():
    p = json.loads((BASE / 'premissas.json').read_text(encoding='utf-8'))
    atual = consumo_kwh(p['unidades'],p['potencia_atual_w'],p['horas_por_dia'],p['dias_por_mes'])
    led = consumo_kwh(p['unidades'],p['potencia_led_w'],p['horas_por_dia'],p['dias_por_mes'])
    economia = atual - led
    kwp = (led/p['rendimento_global_fotovoltaico_hipotese'])/(p['horas_sol_pico_por_dia_hipotese']*p['dias_por_mes'])
    bateria_kwh = (led/p['dias_por_mes'])*p['bateria_autonomia_dias_hipotese']/p['fracao_util_bateria']
    return {'base_kwh_mes':atual,'led_kwh_mes':led,'economia_kwh_mes':economia,
            'economia_pct':100*economia/atual,'economia_led_rs_mes':economia*p['tarifa_rs_kwh'],
            'solar_kwp_minimo_teorico':kwp,'bateria_kwh_nominal_teorica':bateria_kwh,
            'emissoes_evitas_led_kgco2e_ano':economia*12*p['fator_emissao_hipotetico_kgco2e_kwh'],
            'emissoes_evitas_solar_kgco2e_ano':atual*12*p['fator_emissao_hipotetico_kgco2e_kwh']}

if __name__ == '__main__':
    for chave,valor in calcular().items():
        print(f'{chave}: {valor:.2f}')
