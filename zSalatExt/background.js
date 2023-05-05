function updateTabTitle() {
    const now = new Date();
    const timeString = now.toLocaleTimeString();
    chrome.tabs.query({ active: true, currentWindow: true }, function(tabs) {
      if (tabs[0]) {
        chrome.scripting.executeScript({
          target: { tabId: tabs[0].id },
          func: function(timeString) {
            document.title = timeString;
          },
          args: [timeString]
        });
      }
    });
  }
  
  chrome.tabs.onCreated.addListener(function() {
    updateTabTitle();
  });
  
  chrome.tabs.onUpdated.addListener(function() {
    updateTabTitle();
  });
  