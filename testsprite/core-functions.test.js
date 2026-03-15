const { JSDOM } = require('jsdom');
const path = require('path');

// `testsprite_tests` lives inside the `deadlineos` folder, so the HTML fixture is one
// level up from there (inside `deadlineos`).
const htmlPath = path.join(__dirname, '..', 'deadlineos-v3.html');

function waitForLoad(window) {
  return new Promise((resolve) => {
    if (window.document.readyState === 'complete') return resolve();
    window.addEventListener('load', () => resolve());
  });
}

class StorageMock {
  constructor() {
    this._data = Object.create(null);
  }
  get length() {
    return Object.keys(this._data).length;
  }
  key(index) {
    return Object.keys(this._data)[index] || null;
  }
  getItem(key) {
    return Object.prototype.hasOwnProperty.call(this._data, key) ? this._data[key] : null;
  }
  setItem(key, value) {
    this._data[key] = String(value);
  }
  removeItem(key) {
    delete this._data[key];
  }
  clear() {
    this._data = Object.create(null);
  }
}

describe('DeadlineOS core functionality', () => {
  let dom;

  beforeAll(async () => {
    dom = await JSDOM.fromFile(htmlPath, {
      runScripts: 'dangerously',
      resources: 'usable',
      pretendToBeVisual: true,
      beforeParse(window) {
        // jsdom 22 may provide a read-only localStorage/sessionStorage placeholder
        // (often as undefined), so override it with a stable mock.
        Object.defineProperty(window, 'localStorage', {
          value: new StorageMock(),
          configurable: true,
          writable: true,
        });
        Object.defineProperty(window, 'sessionStorage', {
          value: new StorageMock(),
          configurable: true,
          writable: true,
        });
      },
    });

    // Wait for any async scripts to load and run
    await waitForLoad(dom.window);
  });

  afterAll(() => {
    dom.window.close();
  });

  test('should expose `startDemoMode` and populate tasks', async () => {
    expect(typeof dom.window.startDemoMode).toBe('function');

    // Run demo mode to populate tasks and localStorage
    dom.window.startDemoMode();

    const tasksJson = dom.window.localStorage.getItem('dos3-tasks');
    expect(tasksJson).not.toBeNull();

    const tasks = JSON.parse(tasksJson);
    expect(Array.isArray(tasks)).toBe(true);
    expect(tasks.length).toBeGreaterThanOrEqual(1);
    expect(tasks[0]).toHaveProperty('name');
  });

  test('should generate a smart AI response for analysis prompts', () => {
    expect(typeof dom.window._smartMock).toBe('function');

    const tasks = [
      { id: 1, name: 'Test task', urgency: 3, deadline: new Date().toISOString(), done: false },
    ];

    const response = dom.window._smartMock('analyze', tasks, { emoji: '🙂', energy: 6 }, 100, 120);
    expect(typeof response).toBe('string');
    expect(response.length).toBeGreaterThan(10);
    expect(response).toMatch(/(Situation Analysis|Status Report|Deep Analysis|Quick Scan)/);
  });
});
