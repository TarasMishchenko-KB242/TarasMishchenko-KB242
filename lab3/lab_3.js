/**
 * Базовий клас Ticket 
 */
class Ticket {
    constructor(id, name, estimate) {
        this.id = id;
        this.name = name;
        this.estimate = estimate;
        this.completed = false; // Початковий стан - незавершений
    }

    getId() { return this.id; }
    getName() { return this.name; }
    getEstimate() { return this.estimate; }
    
    isCompleted() { return this.completed; }
    
    complete() {
        this.completed = true;
    }
}

/**
 * Клас UserStory 
 */
class UserStory extends Ticket {
    constructor(id, name, estimate, dependencies = []) {
        super(id, name, estimate);
        this.dependencies = dependencies; // Масив інших UserStory
    }

    // Перевизначення методу complete: завершення можливе лише 
    // якщо всі залежності вже завершені
    complete() {
        const allDependenciesCompleted = this.dependencies.every(dep => dep.isCompleted());
        if (allDependenciesCompleted) {
            super.complete();
        } else {
            console.log(`Неможливо завершити US ${this.id}: є незавершені залежності.`);
        }
    }

    getDependencies() {
        return [...this.dependencies]; // Повертаємо копію масиву
    }

    toString() {
        return `[US ${this.id}] ${this.name}`;
    }
}

/**
 * Клас Bug 
 */
class Bug extends Ticket {
    constructor(id, name, estimate, userStory) {
        super(id, name, estimate);
        this.userStory = userStory;
    }

    // Статичний метод для створення бага
    static createBug(id, name, estimate, userStory) {
        // Повертає null, якщо US не існує або не завершена
        if (!userStory || !userStory.isCompleted()) {
            return null;
        }
        return new Bug(id, name, estimate, userStory);
    }

    toString() {
        return `[Bug ${this.id}] ${this.userStory.getName()}: ${this.name}`;
    }
}

/**
 * Клас Sprint - керує плануванням
 */
class Sprint {
    constructor(capacity, ticketsLimit) {
        this.capacity = capacity; // Максимальний сумарний час (estimate)
        this.ticketsLimit = ticketsLimit; // Максимальна кількість тікетів
        this.tickets = [];
    }

    addUserStory(userStory) {
        if (this._canAdd(userStory)) {
            this.tickets.push(userStory);
            return true;
        }
        return false;
    }

    addBug(bug) {
        if (this._canAdd(bug)) {
            this.tickets.push(bug);
            return true;
        }
        return false;
    }

    // Внутрішній метод перевірки обмежень спринту (інкапсуляція логіки)
    _canAdd(ticket) {
        if (!ticket || ticket.isCompleted()) return false;
        
        const totalEstimate = this.getTotalEstimate();
        const fitsCapacity = (totalEstimate + ticket.getEstimate()) <= this.capacity;
        const fitsLimit = this.tickets.length < this.ticketsLimit;

        return fitsCapacity && fitsLimit;
    }

    getTickets() {
        return [...this.tickets]; // Повертаємо захищену копію масиву
    }

    getTotalEstimate() {
        return this.tickets.reduce((sum, ticket) => sum + ticket.getEstimate(), 0);
    }
}

// === ТЕСТУВАННЯ ===

console.log("--- 1. Створення User Stories ---");
const us1 = new UserStory(1, "Реєстрація", 5);
const us2 = new UserStory(2, "Авторизація", 3, [us1]); // Залежить від us1

console.log("Спроба завершити US 2 без US 1:");
us2.complete(); 
console.log(`Статус US 2: ${us2.isCompleted() ? "Завершено" : "В роботі"}`);

us1.complete(); // Завершуємо першу
us2.complete(); // Тепер можна завершити другу
console.log(`Статус US 2 після завершення US 1: ${us2.isCompleted() ? "Завершено" : "В роботі"}`);

console.log("\n--- 2. Створення Bugs ---");
const bug1 = Bug.createBug(1, "Помилка", 2, us2);
console.log(bug1 ? bug1.toString() : "Баг не створено (US не завершена)");

console.log("\n--- 3. Планування Спринту ---");
const sprint = new Sprint(10, 3); // Ємність 10 годин, макс 3 тікети

const task1 = new UserStory(10, "Пошук", 4);
const task2 = new UserStory(11, "Фільтри", 4);
const task3 = new UserStory(12, "Сортування", 5); // Цей не влізе по часу (4+4+5 = 13 > 10)

console.log(`Додано Task 1: ${sprint.addUserStory(task1)}`);
console.log(`Додано Task 2: ${sprint.addUserStory(task2)}`);
console.log(`Додано Task 3: ${sprint.addUserStory(task3)}`);

console.log("\nСписок тікетів у спринті:");
sprint.getTickets().forEach(t => console.log(`- ${t.getName()} (${t.getEstimate()}h)`));
console.log(`Загальний час спринту: ${sprint.getTotalEstimate()}h`);