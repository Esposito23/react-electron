const electron = require("electron");

const app = electron.app;

const BrowserWindow = electron.BrowserWindow;

let mainWindow;

function createWindow() {

    // mainWindow = new BrowserWindow({ alwaysOnTop: true});
    // mainWindow = new BrowserWindow({ kiosk: true });
    mainWindow = new BrowserWindow({ });

    mainWindow.removeMenu();

    mainWindow.loadURL("http://localhost:3000");

    mainWindow.on("closed", () => (mainWindow = null));

}

app.on("ready", createWindow);

app.on("closed", () => {
    app.quit();
});

app.on("activate", () => {
    if (mainWindow === null) {
        createWindow();
    }
});