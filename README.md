# 🐙 Argo Rollouts + Flask + Canary Deployment

Este repositório demonstra uma simulação de **Canary Deployment** utilizando:
- 🐍 **Flask** para a API
- 🐳 **Docker** para containerizar
- ☸️ **Kubernetes** com **Minikube** para orquestração local
- 🚦 **Argo Rollouts** para gerenciar versões progressivas
- 🤖 **GitHub Actions** para CI/CD automatizado

---

## 🚀 Tecnologias Utilizadas

- `Python 3.10` + Flask
- `Docker`
- `Minikube` (Kubernetes local)
- `kubectl` + `kubectl-argo-rollouts`
- `Argo Rollouts`
- `GitHub Actions`

---

## 📁 Estrutura do Projeto

```bash
.
├── app/                          # Código da API Flask
│   ├── main.py
│   └── requirements.txt
├── Dockerfile                    # Build da imagem da API
├── k8s/
│   ├── base/
│   │   ├── deployment.yaml       # (não usado, substituído por rollout)
│   │   └── service.yaml
│   └── canary/
│       ├── rollout.yaml          # Rollout com estratégia Canary
│       └── analysis-template.yaml
└── .github/workflows/deploy.yaml # GitHub Actions para CI/CD
```

---

## ⚙️ Comandos Úteis

### 🛠️ Build da Imagem

```bash
docker build -t flask-app:latest .
```

### 🔁 Apontar Docker local para o Minikube

```bash
eval $(minikube docker-env)
```

### 📦 Aplicar os Manifests

```bash
kubectl apply -f k8s/base/service.yaml
kubectl apply -f k8s/canary/analysis-template.yaml
kubectl apply -f k8s/canary/rollout.yaml
```

### 📊 Verificar o Rollout

```bash
kubectl argo rollouts get rollout flask-rollout --watch
```

### 🌐 Expor a API localmente

```bash
kubectl port-forward svc/flask-app 5000:5000
```

Acesse via navegador em: [http://localhost:5000](http://localhost:5000)

### 🧪 Rodar a Dashboard Web

```bash
kubectl argo rollouts dashboard

Acesse em: [http://localhost:3100](http://localhost:3100)
```
---

## 🧠 Conceitos Usados

- **Canary Deployment**: libera versões novas para apenas uma parte dos usuários, e aumenta gradualmente se tudo estiver saudável.
- **Argo Rollouts**: ferramenta que substitui Deployments por estratégias avançadas como Canary e Blue/Green.
- **AnalysisTemplate**: validações automáticas durante cada etapa do rollout (mesmo sem provider externo, está configurado).
- **GitHub Actions**: pipeline automatizado para CI/CD (estático nesse exemplo).

---

Feito com 💻 por [João Otávio Manieri](https://github.com/JoaoManierii)