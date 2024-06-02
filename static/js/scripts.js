let characters = charactersData;
const slots = document.querySelectorAll('.team-slot, .support-slot');
const characterList = document.getElementById('characterList');
const slotNames = {
    main: ["main-slot1-name", "main-slot2-name", "main-slot3-name", "main-slot4-name"],
    support: ["support-slot1-name", "support-slot2-name", "support-slot3-name", "support-slot4-name"]
};

function openCharacterList(slotIndex, slotType) {
    console.log(`Opening character list for slotIndex: ${slotIndex}, slotType: ${slotType}`);  // デバッグ用ログ
    characterList.style.display = 'block';
    characterList.dataset.slotIndex = slotIndex;
    characterList.dataset.slotType = slotType;
    updateCharacterList();
}

function loadCharacters(attribute) {
    console.log(`Loading characters for attribute: ${attribute}`); // デバッグ用ログ
    const url = `/characters/${attribute}`;
    console.log(`Fetching URL: ${url}`); // デバッグ用ログ
    fetch(url)
        .then(response => {
            console.log(`Response status: ${response.status}`);
            return response.json();
        })
        .then(data => {
            // プロパティ名を正しくマッピング
            characters = data.map(character => ({
                name: character.名前,
                image_path: `static/${attribute}/${character.名前}.png`
            }));
            console.log(`Characters loaded: ${JSON.stringify(characters)}`); // デバッグ用ログ
            updateCharacterList();
        })
        .catch(error => {
            console.error('Error fetching characters:', error);
        });
}

function updateCharacterList() {
    console.log('Updating character list...');  // デバッグ用ログ
    characterList.innerHTML = `
        <div class="attribute-buttons">
            <button class="btn fire" onclick="loadCharacters('火属性')">火</button>
            <button class="btn water" onclick="loadCharacters('水属性')">水</button>
            <button class="btn wind" onclick="loadCharacters('風属性')">風</button>
            <button class="btn light" onclick="loadCharacters('光属性')">光</button>
            <button class="btn dark" onclick="loadCharacters('闇属性')">闇</button>
        </div>
        <div class="character-items">
            ${characters.map(character => `
                <div class="character-item" onclick="selectCharacter('${character.name}', '${character.image_path}')">
                    <img src="${character.image_path}" alt="${character.name}">
                </div>
            `).join('')}
        </div>
    `;
}

function selectCharacter(name, imagePath) {
    console.log(`Selecting character: ${name}, imagePath: ${imagePath}`);  // デバッグ用ログ
    const slotIndex = characterList.dataset.slotIndex;
    const slotType = characterList.dataset.slotType;
    const slotName = slotNames[slotType][slotIndex];
    const slotElement = document.getElementById(slotName);
    
    if (slotType === 'main') {
        slots[slotIndex * 2].innerHTML = `<img src="${imagePath}" alt="${name}">`;
    } else if(slotType === 'support'){
        slots[slotIndex * 2 + 1].innerHTML = `<img src="${imagePath}" alt="${name}">`;
    }

    characterList.style.display = 'none';
}

document.addEventListener('click', function(event) {
    if (!characterList.contains(event.target) && event.target.closest('.team-slot, .support-slot') === null) {
        characterList.style.display = 'none';
    }
});

// 初期ロード時に火属性のキャラクターをロード
loadCharacters('火属性');
