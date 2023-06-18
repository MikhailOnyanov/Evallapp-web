import {writeMsg} from "./customLog.js";

export var savedValue;

export function saveValue(ev) {
    if (ev.target.tagName === 'TD') {
        savedValue = ev.target.textContent;
    }
    return void 0;
}


export async function updateSaved(ev) {
    if (ev.target.tagName === 'TD') {
        if (savedValue !== ev.target.textContent) {
            console.log(
                JSON.stringify({
                    id: ev.target.dataset.elementId,
                    [ev.target.dataset.columnId]: ev.target.textContent
                })
            );
            let tableName = document.querySelector('#database-name-option').value;
            let api_url = ev.currentTarget.customApi;
            writeMsg(`Таблица для изменения: ${tableName}`, 0);
            try {
                const response = await fetch(api_url, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        id: ev.target.dataset.elementId,
                        table_name: tableName,
                        data: {[ev.target.dataset.columnId]: ev.target.textContent}
                    }),
                });
                response.status === 200 ? writeMsg(await response.text(), 0): writeMsg(await response.text(), 1);
            } catch (err) {
                writeMsg(err, 2);
            }

        }
        savedValue = undefined;
    }
}

export function enterVal(ev) {
    if (ev.target.tagName === 'TD') {
        if (ev.key === 'Escape') {
            ev.target.textContent = savedValue;
            ev.target.blur();
        } else if (ev.key === 'Enter') {
            ev.preventDefault();
            ev.target.blur();
        }
    }
}

