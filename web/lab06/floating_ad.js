// floating_ad.js - 飘动窗口JavaScript代码

// 1. addEvent 函数 (用于跨浏览器事件处理)
function addEvent(obj, evtType, func, cap) {
  cap = cap || false;
  if (obj.addEventListener) {
    obj.addEventListener(evtType, func, cap);
  } else if (obj.attachEvent) {
    // 兼容 IE
    obj.attachEvent("on" + evtType, func);
  } else {
    // 更早的浏览器或备用方案
    obj["on" + evtType] = func;
  }
}

// 2. GetPageSize 函数 (用于获取页面及窗口尺寸)
function GetPageSize() {
  var windowWidth, windowHeight;
  var pageWidth, pageHeight;
  var xScroll, yScroll;

  if (window.innerHeight && window.scrollMaxY) {
    xScroll = window.innerWidth + window.scrollMaxX;
    yScroll = window.innerHeight + window.scrollMaxY;
  } else if (document.body.scrollHeight > document.body.offsetHeight) {
    xScroll = document.body.scrollWidth;
    yScroll = document.body.scrollHeight;
  } else {
    xScroll = document.body.offsetWidth;
    yScroll = document.body.offsetHeight;
  }

  if (self.innerHeight) {
    // all except Explorer
    if (document.documentElement && document.documentElement.clientWidth) {
      // Explorer 6 Strict Mode also uses this
      windowWidth = document.documentElement.clientWidth;
    } else {
      windowWidth = self.innerWidth; // Others
    }
    windowHeight = self.innerHeight;
  } else if (
    document.documentElement &&
    document.documentElement.clientHeight
  ) {
    // Explorer 6 Strict Mode
    windowWidth = document.documentElement.clientWidth;
    windowHeight = document.documentElement.clientHeight;
  } else if (document.body) {
    // other Explorers
    windowWidth = document.body.clientWidth;
    windowHeight = document.body.clientHeight;
  }

  // for page height
  if (yScroll < windowHeight) {
    pageHeight = windowHeight;
  } else {
    pageHeight = yScroll;
  }

  // for page width
  if (xScroll < windowWidth) {
    pageWidth = windowWidth;
  } else {
    pageWidth = xScroll;
  }
  var arrayPageSize = new Array(
    pageWidth,
    pageHeight,
    windowWidth,
    windowHeight
  );
  return arrayPageSize;
}

// 3. getPageScroll 函数 (用于获取页面滚动距离)
function getPageScroll() {
  var xScroll, yScroll;
  if (typeof window.pageYOffset == "number") {
    // Netscape compliant
    yScroll = window.pageYOffset;
    xScroll = window.pageXOffset;
  } else if (
    document.body &&
    (document.body.scrollLeft || document.body.scrollTop)
  ) {
    // DOM compliant
    yScroll = document.body.scrollTop;
    xScroll = document.body.scrollLeft;
  } else if (
    document.documentElement &&
    (document.documentElement.scrollLeft || document.documentElement.scrollTop)
  ) {
    // IE6 Strict
    yScroll = document.documentElement.scrollTop;
    xScroll = document.documentElement.scrollLeft;
  } else {
    // Fallback
    yScroll = 0;
    xScroll = 0;
  }
  var arrayScroll = new Array(xScroll, yScroll);
  return arrayScroll;
}

// 4. AdMoveConfig 对象 (用于配置漂浮广告的参数)
var AdMoveConfig = new Object();
AdMoveConfig.IsInitialized = false;
AdMoveConfig.ScrollX = 0;
AdMoveConfig.ScrollY = 0;
AdMoveConfig.MoveWidth = 0;
AdMoveConfig.MoveHeight = 0;

AdMoveConfig.Resize = function () {
  var winsize = GetPageSize();
  AdMoveConfig.MoveWidth = winsize[2]; // windowWidth
  AdMoveConfig.MoveHeight = winsize[3]; // windowHeight
  AdMoveConfig.Scroll(); // 更新滚动位置
};

AdMoveConfig.Scroll = function () {
  var winscroll = getPageScroll();
  AdMoveConfig.ScrollX = winscroll[0];
  AdMoveConfig.ScrollY = winscroll[1];
};

// 5. 为 window 绑定 resize 和 scroll 事件
addEvent(window, "resize", AdMoveConfig.Resize);
addEvent(window, "scroll", AdMoveConfig.Scroll);

// 6. AdMove 构造函数 (实现漂浮逻辑)
function AdMove(id) {
  if (!AdMoveConfig.IsInitialized) {
    AdMoveConfig.Resize();
    AdMoveConfig.IsInitialized = true;
  }
  var obj = document.getElementById(id);
  obj.style.position = "absolute";

  var W = AdMoveConfig.MoveWidth - obj.offsetWidth;
  var H = AdMoveConfig.MoveHeight - obj.offsetHeight;
  var x = W * Math.random(),
    y = H * Math.random();
  var rad = ((Math.random() + 1) * Math.PI) / 6;
  var kx = Math.sin(rad),
    ky = Math.cos(rad);
  var dirx = Math.random() < 0.5 ? 1 : -1,
    diry = Math.random() < 0.571 ? -1 : 1;

  var step = 1;
  var interval;

  // this.SetDirection
  this.SetDirection = function (vx, vy) {
    x = vx;
    y = vy;
  };

  // this.CustomMethod
  this.CustomMethod = function () {
    obj.style.left = x + AdMoveConfig.ScrollX + "px";
    obj.style.top = y + AdMoveConfig.ScrollY + "px";

    rad = ((Math.random() + 1) * Math.PI) / 6;
    W = AdMoveConfig.MoveWidth - obj.offsetWidth; // Recalculate W, H in case of resize
    H = AdMoveConfig.MoveHeight - obj.offsetHeight;

    x = x + step * kx * dirx;
    if (x < 0) {
      dirx = 1;
      x = 0;
      kx = Math.sin(rad);
      ky = Math.cos(rad);
    }
    if (x > W) {
      dirx = -1;
      x = W;
      kx = Math.sin(rad);
      ky = Math.cos(rad);
    }

    y = y + step * ky * diry;
    if (y < 0) {
      diry = 1;
      y = 0;
      kx = Math.sin(rad);
      ky = Math.cos(rad);
    }
    if (y > H) {
      diry = -1;
      y = H;
      kx = Math.sin(rad);
      ky = Math.cos(rad);
    }
  };

  // this.Run
  this.Run = function () {
    var delay = 10;
    var self = this; // 修正this指向问题
    interval = setInterval(function () {
      self.CustomMethod();
    }, delay);
    obj.onmouseover = function () {
      clearInterval(interval);
    };
    obj.onmouseout = function () {
      interval = setInterval(function () {
        self.CustomMethod();
      }, delay);
    };
  };
}
