# Docker reset helper for the project
# Usage: .\docker-reset.ps1

Write-Host "Stopping and removing containers, volumes, and networks..."
docker compose down -v

Write-Host "Starting services in a fresh seeded state..."
docker compose up --build -d

Write-Host "Docker compose restart complete. Verify services at http://localhost:8080, http://localhost:5000, and http://localhost:5173"
