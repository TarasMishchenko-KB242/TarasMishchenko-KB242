const readline = require('readline');

// Налаштування для зчитування з консолі
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const question = (query) => new Promise((resolve) => rl.question(query, resolve));

// --- ЗАВДАННЯ 1: Привітання ---
async function task1() {
    console.log("\n--- Завдання 1 ---");
    const name = await question("Введіть рядок: ");
    console.log(`Hello, ${name}`);
}

// --- ЗАВДАННЯ 2: Електронний годинник ---
async function task2() {
    console.log("\n--- Завдання 2 ---");
    const input = await question("Введіть секунди: ");
    let totalSeconds = parseInt(input);
    
    let h = Math.floor(totalSeconds / 3600) % 24;
    let m = Math.floor((totalSeconds % 3600) / 60);
    let s = totalSeconds % 60;

    const pad = (n) => n < 10 ? '0' + n : n;
    console.log(`Час: ${h}:${pad(m)}:${pad(s)}`);
}

// --- ЗАВДАННЯ 3: Пароль ---
const SECRET_PASSWORD = 1234;
async function task3() {
    console.log("\n--- Завдання 3 ---");
    const input = await question("Введіть пароль: ");
    if (parseInt(input) === SECRET_PASSWORD) {
        console.log("Hello, Agent");
    } else {
        console.log("Access denied");
    }
}

// --- ЗАВДАННЯ 4: Незнайомці ---
async function task4() {
    console.log("\n--- Завдання 4 ---");
    const nInput = await question("Скільки незнайомців зустріти? ");
    const n = parseInt(nInput);

    if (n < 0) return console.log("Кількість не може бути від’ємною");
    if (n === 0) return console.log("Немає з ким зустрітися");

    for (let i = 0; i < n; i++) {
        const name = await question(`Ім'я ${i + 1}-го незнайомця: `);
        console.log(`Hello, ${name}`);
    }
}

// --- ЗАВДАННЯ 5: Равлик ---
async function task5() {
    console.log("\n--- Завдання 5 ---");
    const input = await question("Введіть a, b, h (через пробіл): ");
    const [a, b, h] = input.split(' ').map(Number);

    if (a >= h) {
        console.log("Результат: 1");
    } else if (a <= b) {
        console.log("Результат: Impossible");
    } else {
        const days = Math.ceil((h - a) / (a - b)) + 1;
        console.log(`Результат: ${days}`);
    }
}

// --- ЗАВДАННЯ 6: Ресторан ---
async function task6() {
    console.log("\n--- Завдання 6 ---");
    const input = await question("Введіть суму та к-сть друзів: ");
    const [total, friends] = input.split(' ').map(Number);

    if (total < 0 || friends <= 0) {
        console.log("Некоректні дані");
    } else {
        const bill = (total * 1.10) / friends;
        console.log(`Кожен платить: ${Math.round(bill)}`);
    }
}

// --- ЗАВДАННЯ 7 ТА 8: Послідовність (Максимум та Середнє) ---
async function task7and8() {
    console.log("\n--- Завдання 7 та 8 ---");
    console.log("Вводьте числа (0 - кінець):");
    let max = -Infinity;
    let sum = 0;
    let count = 0;

    while (true) {
        const num = parseInt(await question("> "));
        if (num === 0) break;
        if (num > max) max = num;
        sum += num;
        count++;
    }

    if (count > 0) {
        console.log(`Максимум (Завд. 7): ${max}`);
        console.log(`Середнє (Завд. 8): ${sum / count}`);
    }
}

// --- ЗАВДАННЯ 9: Квадратне рівняння ---
async function task9() {
    console.log("\n--- Завдання 9 ---");
    const input = await question("Введіть a, b, c: ");
    const [a, b, c] = input.split(' ').map(Number);
    const d = b * b - 4 * a * c;

    if (d < 0) console.log("no roots");
    else if (d === 0) console.log(`Корінь: ${-b / (2 * a)}`);
    else {
        const x1 = (-b - Math.sqrt(d)) / (2 * a);
        const x2 = (-b + Math.sqrt(d)) / (2 * a);
        console.log(`Корені: ${x1} ${x2}`);
    }
}

// --- ЗАВДАННЯ 10-14: Функції масивів (Демонстрація) ---
function arrayTasksDemo() {
    console.log("\n--- Завдання 10-14 (Демонстрація масивів) ---");
    const testArr = [1, -1, 0, 4, 6, 10, 15, 25];
    console.log("Масив:", testArr);

    // Завдання 10
    const maxVal = (arr) => Math.max(...arr);
    console.log("10. Максимум:", maxVal(testArr));

    // Завдання 11
    const sumEven = (arr) => arr.filter(x => x % 2 === 0).reduce((a, b) => a + b, 0);
    console.log("11. Сума парних:", sumEven(testArr));

    // Завдання 12
    const getSumCheck = (arr) => {
        let res = [false, false];
        for(let i=2; i<arr.length; i++) res.push(arr[i] === arr[i-1] + arr[i-2]);
        return res;
    };
    console.log("12. Перевірка суми попередніх:", getSumCheck(testArr));

    // Завдання 13
    const removeMaxima = (arr) => arr.filter((v, i) => {
        const left = i === 0 || v <= arr[i-1];
        const right = i === arr.length - 1 || v <= arr[i+1];
        return left || right;
    });
    console.log("13. Без локальних максимумів:", removeMaxima([18, 1, 3, 6, 7, -5]));

    // Завдання 14
    const cycleSwap = (arr, shift = 1) => {
        const s = shift % arr.length;
        return [...arr.slice(-s), ...arr.slice(0, -s)];
    };
    console.log("14. Циклічний зсув (3):", cycleSwap([1, 3, 2, 7, 4], 3));
}

// --- ГОЛОВНИЙ ЗАПУСК ---
async function main() {
    try {
        await task1();
        await task2();
        await task3();
        await task4();
        await task5();
        await task6();
        await task7and8();
        await task9();
        arrayTasksDemo();
    } catch (err) {
        console.error(err);
    } finally {
        console.log("\nЛабораторна робота завершена.");
        rl.close();
    }
}

main();