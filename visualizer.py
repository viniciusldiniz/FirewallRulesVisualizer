import subprocess
import platform
import re
import sys

def get_firewall_rules():
    os_name = platform.system()

    if os_name == "Linux":
        try:
            result = subprocess.check_output(["sudo", "iptables", "-L", "-n", "-v"], text=True)
            return result
        except Exception as e:
            print(f"Erro ao obter regras do iptables: {e}")
    elif os_name == "Windows":
        try:
            result = subprocess.check_output(
                ["netsh", "advfirewall", "firewall", "show", "rule", "name=all"], text=True
            )
            return result
        except Exception as e:
            print(f"Erro ao obter regras do Windows Firewall: {e}")
    else:
        print("Sistema operacional não suportado.")
        sys.exit(1)

def parse_rules_to_html(raw_rules):
    html_content = f"""
    <html>
    <head>
        <title>Visualização de Regras de Firewall</title>
        <style>
            body {{ font-family: Arial; background: #f9f9f9; padding: 20px; }}
            h1 {{ color: #333; }}
            pre {{ background: #eee; padding: 10px; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>🔐 Visualização de Regras de Firewall</h1>
        <pre>{raw_rules}</pre>
    </body>
    </html>
    """
    with open("firewall_rules.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✅ Arquivo 'firewall_rules.html' gerado com sucesso.")

if __name__ == "__main__":
    rules = get_firewall_rules()
    if rules:
        parse_rules_to_html(rules)
