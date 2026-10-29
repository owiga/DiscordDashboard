async function updatePresence() {
    try {
        let response = await fetch('/api/presence');
        let data = await response.json();

        const container = document.getElementById('presence-container');
        if (!container) return;

        // Если активность есть — рисуем, если нет — пишем, что тихо
        if (data.activities && data.activities.length > 0) {
            let html = '';
            data.activities.forEach(act => {
                if (act.type === 2) {
                    html += `
                        <div class="flex items-center gap-2">
                            <span class="inline-block w-3 h-3 rounded-full bg-emerald-400 animate-pulse"></span>
                            <span class="text-sm text-purple-200/60 mt-1 italic">Listening ${act.state || ''} - ${act.details || act.name}</span>
                        </div>
                    `;
                }
                // Здесь можно дописать условия для других типов (игры и т.д.)
            });
            container.innerHTML = html;
        } else {
            container.innerHTML = `<span class="text-white/40 text-sm">No activity</span>`;
        }

    } catch (error) {
        console.error("Ошибка при обновлении статуса:", error);
    }
}

// Запускаем опрос каждые 5 секунд
setInterval(updatePresence, 5000);