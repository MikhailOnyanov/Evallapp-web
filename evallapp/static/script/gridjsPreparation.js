const editableCellAttributes = (data, row, col) => {
    if (row) {
        return {contentEditable: 'true', 'data-element-id': row.cells[0].data};
    } else {
        return {};
    }
};

async function getFullDatasetByName(name, api_url) {
    let host_url = 'http://localhost:5000'
    let request_url = host_url + api_url + '?' + new URLSearchParams({db_name: name});
    console.log(request_url);
    let response = await fetch(request_url);
    return await response.json()
}

import {
    Grid,
    h
} from "./gridjs.js";

export async function getPreparedDatasetByName(name, api_url, prepareBool) {
    const dataset = await getFullDatasetByName(name, api_url);
    try {
        if (prepareBool) {
            for (const prop in dataset.columns) {
                dataset.columns[prop]['attributes'] = editableCellAttributes;
            }
            dataset.columns.push(
                {
                    name: 'Действия',
                    formatter: (cell, row) => {
                        return h('button', {
                            className: 'btn btn-secondary',
                            onClick: () => alert(`Editing "${row.cells[0].data}" "${row.cells[1].data}"`)
                        }, 'Удалить');
                    }
                }
            );
        } else return dataset
        return dataset
    }
    catch (ex) {
        console.log(ex)
        return dataset
    }
}

