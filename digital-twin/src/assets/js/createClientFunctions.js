const online = new Event("isonline");

async function newClient(cameraid, ip, port) {
  client = new SJMPClient(cameraid);
  client.type = type;
  client.start(ip, port);
}

async function createAndConnectClient(cameraid, ip, port) {
  if (cameraid != "" && cameraid != "" && port >= 0 && port <= 65535) {
    lockConfig();
    await newClient(cameraid, ip, port);
  } else {
    alert("[ERROR] Please insert all values!");
  }
}
function waitToClose() {
  if (client.socket.bufferedAmount > 0) {
    client.close();
  } else {
    setTimeout(waitForElement, 250);
  }
}

async function createAndConnectClientToClients(
  text,
  CAMERAS,
  cameraid,
  ip,
  port,
  count = null,
  wait = null
) {
  await createAndConnectClient(cameraid, ip, port);

  if (wait != null) {
    let res = parseInt(wait);
    if (isNaN(res) || res <= 0) {
      alert("Wait seconds must be higher than 0 and must be a number");
      wait = null;
    }
  }

  if (count != null) {
    let res = parseInt(count);
    if (isNaN(res) || res <= 0) {
      alert("Count must be higher than 0 and must be a number");
      count = 1;
    }
  }

  const clientsList = CAMERAS.split("|");
  if (clientsList == null) {
    alert("[FAIL] You must indicate CAMERAS!");
    return;
  }

  clientsList.forEach(async function (value) {
    document.addEventListener(
      "isonline",
      async function (e) {
        let i = 0;
        while (i < count) {
          client.sendMessageToClient(value, text + i.toString());

          if (wait != null) {
            await sleep(wait);
          }

          i++;
        }
      },
      false
    );
  });
}

async function createAndConnectClientWithText(
  text,
  cameraid,
  ip,
  port,
  count = 1,
  wait = null
) {
  await createAndConnectClient(cameraid, ip, port);

  if (wait != null) {
    var res = parseInt(wait);
    if (isNaN(res) || res <= 0) {
      alert("Wait seconds must be higher than 0 and must be a number");
      wait = null;
    }
  }
  if (count != 1) {
    var res = parseInt(count);
    if (isNaN(res) || res <= 0) {
      alert("Count must be higher than 0 and must be a number");
      count = 1;
    }
  }

  if (text == null) {
    text = "Test String 1234";
  }

  // Listen for the event.
  document.addEventListener(
    "isonline",
    async function (e) {
      let i = 0;
      while (i < count) {
        client.sendMessageToServer(text + i.toString());

        if (wait != null) {
          await sleep(wait);
        }

        i++;
      }

      waitToClose();
    },
    false
  );
}
