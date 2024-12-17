function fillFilmList() {
    fetch('/lab7/rest-api/films/')
        .then(response => response.json())
        .then(films => {
            let tbody = document.getElementById('film-list');
            tbody.innerHTML = '';
            films.forEach(film => {
                let tr = document.createElement('tr');

                let tdTitleRus = document.createElement('td');
                let tdTitle = document.createElement('td');
                let tdYear = document.createElement('td');
                let tdAction = document.createElement('td');

                tdTitleRus.innerText = film.title_ru;
                let originalTitle = document.createElement('span');
                originalTitle.innerText = film.title === film.title_ru ? '' : `(${film.title})`;
                originalTitle.style.fontStyle = 'italic';
                tdTitle.appendChild(originalTitle);
                tdYear.innerText = film.year;

                let editButton = document.createElement('button');
                editButton.innerText = 'редактировать';
                editButton.onclick = () => editFilm(film.id);

                let delButton = document.createElement('button');
                delButton.innerText = 'удалить';
                delButton.onclick = () => deleteFilm(film.id, film.title_ru);

                tdAction.append(editButton, delButton);

                tr.append(tdTitleRus, tdTitle, tdYear, tdAction);
                tbody.append(tr);
            });
        });
}

function deleteFilm(id, title) {
    if (!confirm(`Вы точно хотите удалить фильм "${title}"?`)) return;

    fetch(`/lab7/rest-api/films/${id}`, { method: 'DELETE' })
        .then(() => fillFilmList());
}

function sendFilm() {
    const film = {
        title: document.getElementById('title').value.trim(),
        title_ru: document.getElementById('title-ru').value.trim(),
        year: document.getElementById('year').value.trim(),
        description: document.getElementById('description').value.trim()
    };

    const id = document.getElementById('id').value;
    const url = id ? `/lab7/rest-api/films/${id}` : '/lab7/rest-api/films/';
    const method = id ? 'PUT' : 'POST';

    fetch(url, {
        method: method,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(film)
    })
        .then(response => {
            if (response.ok) {
                fillFilmList();
                hideModal();
            } else {
                return response.json().then(errors => {
                    // Отображаем ошибки рядом с соответствующими полями
                    document.getElementById('title-ru-error').innerText = errors.title_ru || '';
                    document.getElementById('title-error').innerText = errors.title || '';
                    document.getElementById('year-error').innerText = errors.year || '';
                    document.getElementById('description-error').innerText = errors.description || '';
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Произошла ошибка при отправке данных');
        });
}

function editFilm(id) {
    fetch(`/lab7/rest-api/films/${id}`)
        .then(response => response.json())
        .then(film => {
            document.getElementById('id').value = film.id;
            document.getElementById('title').value = film.title;
            document.getElementById('title-ru').value = film.title_ru;
            document.getElementById('year').value = film.year;
            document.getElementById('description').value = film.description;
            showModal();
        });
}

function showModal() {
    document.querySelector('div.modal').style.display = 'block';
}

function hideModal() {
    document.querySelector('div.modal').style.display = 'none';
}

function cancel() {
    hideModal();
}

function addFilm() {
    document.getElementById('id').value = '';
    document.getElementById('title').value = '';
    document.getElementById('title-ru').value = '';
    document.getElementById('year').value = '';
    document.getElementById('description').value = '';
    showModal();
}

fillFilmList();


