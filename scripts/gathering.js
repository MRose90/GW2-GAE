var app = angular
.module("nodeApp", [])
.controller("node-cont", function($scope) {
  $scope.nodeList = [
    { type: "v", name: "[&BE8BAAA=]" },
    { type: "i", name: "[&BEsBAAA=]" },
    { type: "g", name: "[&BEwBAAA=]" },
    { type: "s", name: "[&BNgAAAA=]" },
    { type: "i", name: "[&BFEDAAA=]" },
    { type: "v", name: "[&BAACAAA=]" },
    { type: "g", name: "[&BAECAAA=]" },
    { type: "se", name: "[&BAECAAA=]" },
    { type: "se", name: "[&BAMCAAA=]" },
    { type: "p", name: "[&BO8BAAA=]" },
    { type: "p", name: "[&BO4BAAA=]" },
    { type: "v", name: "[&BOwBAAA=]" },
    { type: "v", name: "[&BMcDAAA=]" },
    { type: "c", name: "[&BIQBAAA=]" },
    { type: "c", name: "[&BPgGAAA=]" },
    { type: "so", name: "[&BMUDAAA=]" },
    { type: "s", name: "[&BNoAAAA=]" },
    { type: "i", name: "[&BF4BAAA=]" },
    { type: "v", name: "[&BN4AAAA=]" },
    { type: "ha", name: "[&BB0CAAA=]" },
    { type: "v", name: "[&BB0CAAA=]" },
    { type: "p", name: "[&BBoCAAA=]" },
    { type: "m", name: "[&BEAFAAA=]" },
    { type: "p", name: "[&BB8CAAA=]" },
    { type: "v", name: "[&BHgCAAA=]" },
    { type: "m", name: "[&BHkCAAA=]" },
    { type: "i", name: "[&BMAAAAA=]" },
    { type: "v", name: "[&BMAAAAA=]" },
    { type: "s", name: "[&BMADAAA=]" },
    { type: "i", name: "[&BFEGAAA=]" },
    { type: "s", name: "[&BOkAAAA=]" },
    { type: "v", name: "[&BOYAAAA=]" },
    { type: "g", name: "[&BOYAAAA=]" },
    { type: "so", name: "[&BOUAAAA=]" },
    { type: "se", name: "[&BGICAAA=]" },
    { type: "i", name: "[&BGUCAAA=]" },
    { type: "v", name: "[&BF8CAAA=]" },
    { type: "so", name: "[&BF8CAAA=]" },
    { type: "so", name: "[&BFoCAAA=]" },
    { type: "so", name: "[&BFsCAAA=]" },
    { type: "g", name: "[&BFsCAAA=]" },
    { type: "p", name: "[&BFECAAA=]" },
    { type: "v", name: "[&BFECAAA=]" },
    { type: "ha", name: "[&BEwCAAA=]" },
    { type: "ha", name: "[&BE0CAAA=]" },
    { type: "ha", name: "[&BEUCAAA=]" },
    { type: "ha", name: "[&BNACAAA=]" },
    { type: "he", name: "[&BNMCAAA=]" },
    { type: "v", name: "[&BNECAAA=]" },
    { type: "p", name: "[&BNQCAAA=]" },
    { type: "p", name: "[&BMkCAAA=]" },
    { type: "ha", name: "[&BMcCAAA=]" },
    { type: "v", name: "[&BFgGAAA=]" },
    { type: "e", name: "[&BFgGAAA=]" },
    { type: "m", name: "[&BOUGAAA=]" },
    { type: "e", name: "[&BPgCAAA=]" },
    { type: "e", name: "[&BKYCAAA=]" },
    { type: "m", name: "[&BKgCAAA=]" },
    { type: "m", name: "[&BLICAAA=]" },
    { type: "ea", name: "[&BB4DAAA=]" },
    { type: "m", name: "[&BOQGAAA=]" },
    { type: "p", name: "[&BMwBAAA=]" },
    { type: "v", name: "[&BMkBAAA=]" },
    { type: "p", name: "[&BMkBAAA=]" },
    { type: "p", name: "[&BK0BAAA=]" },
    { type: "v", name: "[&BKcBAAA=]" },
    { type: "i", name: "[&BJMBAAA=]" },
    { type: "s", name: "[&BJMBAAA=]" },
    { type: "v", name: "[&BOQAAAA=]" },
    { type: "g", name: "[&BLEAAAA=]" },
    { type: "ss", name: "[&BK8AAAA=]" },
    { type: "ss", name: "[&BKgAAAA=]" },
    { type: "i", name: "[&BKsAAAA=]" },
    { type: "v", name: "[&BKsAAAA=]" },
    { type: "v", name: "[&BPoAAAA=]" },
    { type: "c", name: "[&BPMAAAA=]" },
    { type: "c", name: "[&BPcAAAA=]" },
    { type: "mix", name: "[&BAQAAAA=]" },
    { type: "v", name: "[&BBIAAAA=]" },
    { type: "mix", name: "[&BBIAAAA=]" },
    { type: "mix", name: "[&BBIAAAA=]" },
    { type: "v", name: "[&BNUGAAA=]" },
    { type: "m", name: "[&BNUGAAA=]" },
    { type: "o", name: "[&BNgGAAA=]" },
    { type: "c", name: "[&BDwBAAA=]" },
    { type: "v", name: "[&BEIAAAA=]" },
    { type: "v", name: "[&BEABAAA=]" },
    { type: "c", name: "[&BEEBAAA=]" },
    { type: "v", name: "[&BFwAAAA=]" },
    { type: "v", name: "[&BHUAAAA=]" },
    { type: "so", name: "[&BGEAAAA=]" },
    { type: "i", name: "[&BGMAAAA=]" },
    { type: "s", name: "[&BGMAAAA=]" },
    { type: "v", name: "[&BIYHAAA=]" },
    { type: "q", name: "[&BHoHAAA=]" },
    { type: "q", name: "[&BHoHAAA=]" },
    { type: "v", name: "[&BOAHAAA=]" },
    { type: "m", name: "[&BOAHAAA=]" },
    { type: "o", name: "[&BGwIAAA=]" },
    { type: "an", name: "[&BGwIAAA=]" },
    { type: "v", name: "[&BA4IAAA=]" },
    { type: "v", name: "[&BF8JAAA=]" }
  ];
  $scope.shortTypes = [
    "c",
    "s",
    "i",
    "g",
    "p",
    "m",
    "o",
    "q",
    "v",
    "so",
    "se",
    "ha",
    "e",
    "an"
  ];
  $scope.types = {
    c: {order: 1, val: true, file: 'images/40px-Copper_Ore.png'},
    s: {order: 2, val: true, file: 'images/40px-Silver_Ore.png'},
    i: {order: 3, val: true, file: 'images/40px-Iron_Ore.png'},
    g: {order: 4, val: true, file: 'images/40px-Gold_Ore.png'},
    p: {order: 5, val: true, file: 'images/40px-Platinum_Ore.png'},
    m: {order: 6, val: true, file: 'images/40px-Mithril_Ore.png'},
    o: {order: 7, val: true, file: 'images/40px-Orichalcum_Ore.png'},
    q: {order: 8, val: true, file: 'images/40px-Quartz_Crystal.png'},
    v: {order: 9, val: true, file: 'images/40px-Spinach_Leaf.png'},
    so: {order: 10, val: true, file: 'images/40px-Soft_Wood_Log.png' },
    se: {order: 11, val: true, file: 'images/40px-Seasoned_Wood_Log.png'},
    ha: {order: 12, val: true, file: 'images/40px-Hard_Wood_Log.png'},
    e: {order: 13, val: true, file: 'images/40px-Elder_Wood_Log.png'},
    an: {order: 14, val: true, file: 'images/40px-Ancient_Wood_Log.png'}
  };
  $scope.doNodeList = function() {
    // In this case, it may actually be easier NOT to use ng-repeat's filter
    $scope.motd = "";
    $scope.chat = "";
    $scope.unformatted = "";
    $scope.count = 0;
    $scope.nodeList.forEach(function(n) {
      console.log(n.type);
      if ($scope.types[n.type] && $scope.types[n.type].val) {
        if(!($scope.count % 3)){
          if($scope.count !== 0){
            $scope.motd = $scope.motd.concat('\n');
          }
          $scope.motd = $scope.motd.concat((($scope.count/ 3)+1) +'.')
        }
        if(!($scope.count % 17)){
          if($scope.count !== 0){
            $scope.chat = $scope.chat.concat('\n');
          }
          $scope.chat = $scope.chat.concat((($scope.count/ 17)+1) +'.')
        }
        $scope.count += 1;
        $scope.motd = $scope.motd.concat(n.name);
        
        $scope.chat = $scope.chat.concat(n.name);
        $scope.unformatted = $scope.unformatted.concat(n.name);
      } else if (n.type === 'ea'&&(($scope.types['e'] && $scope.types['e'].val) ||($scope.types['an'] && $scope.types['an'].val))) {
        if(!($scope.count % 48) && $scope.count !== 0){
            $scope.motd = $scope.motd.concat('\r');
        }
          if(!($scope.count % 3)){
          if($scope.count !== 0){
            $scope.motd = $scope.motd.concat('\n');
          }
          $scope.motd = $scope.motd.concat((($scope.count/ 3)+1) +'.')
        }
        if(!($scope.count % 17)){
          if($scope.count !== 0){
            $scope.chat = $scope.chat.concat('\r\n');
          }
          $scope.chat = $scope.chat.concat((($scope.count/ 17)+1) +'.')
        }
        $scope.count += 1;
        $scope.motd = $scope.motd.concat(n.name);
        
        $scope.chat = $scope.chat.concat(n.name);
        $scope.unformatted = $scope.unformatted.concat(n.name);
      }else if (n.type === 'he'&&(($scope.types['e'] && $scope.types['e'].val) ||($scope.types['ha'] && $scope.types['ha'].val))) {
        if(!($scope.count % 3)){
          if($scope.count !== 0){
            $scope.motd = $scope.motd.concat('\n');
          }
          $scope.motd = $scope.motd.concat((($scope.count/ 3)+1) +'.')
        }
        if(!($scope.count % 17)){
          if($scope.count !== 0){
            $scope.chat = $scope.chat.concat('\n');
          }
          $scope.chat = $scope.chat.concat((($scope.count/ 17)+1) +'.')
        }
        $scope.count += 1;
        $scope.motd = $scope.motd.concat(n.name);
        
        $scope.chat = $scope.chat.concat(n.name);
        $scope.unformatted = $scope.unformatted.concat(n.name);
      }
      else if (n.type === 'mix'&&(($scope.types['i'] && $scope.types['i'].val) ||($scope.types['s'] && $scope.types['s'].val))) {
        if(!($scope.count % 3)){
          if($scope.count !== 0){
            $scope.motd = $scope.motd.concat('\n');
          }
          $scope.motd = $scope.motd.concat((($scope.count/ 3)+1) +'.')
        }
        if(!($scope.count % 17)){
          if($scope.count !== 0){
            $scope.chat = $scope.chat.concat('\n');
          }
          $scope.chat = $scope.chat.concat((($scope.count/ 17)+1) +'.')
        }
        $scope.count += 1;
        $scope.motd = $scope.motd.concat(n.name);
        
        $scope.chat = $scope.chat.concat(n.name);
        $scope.unformatted = $scope.unformatted.concat(n.name);
      }
      else if (n.type === 'ss'&&(($scope.types['se'] && $scope.types['se'].val) ||($scope.types['so'] && $scope.types['so'].val))) {
        if(!($scope.count % 3)){
          if($scope.count !== 0){
            $scope.motd = $scope.motd.concat('\n');
          }
          $scope.motd = $scope.motd.concat((($scope.count/ 3)+1) +'.')
        }
        if(!($scope.count % 17)){
          if($scope.count !== 0){
            $scope.chat = $scope.chat.concat('\n');
          }
          $scope.chat = $scope.chat.concat((($scope.count/ 17)+1) +'.')
        }
        $scope.count += 1;
        $scope.motd = $scope.motd.concat(n.name);
        
        $scope.chat = $scope.chat.concat(n.name);
        $scope.unformatted = $scope.unformatted.concat(n.name);
      }
    });
  };
  $scope.doNodeList();
  $scope.doAllType = function(t){
    console.log(t,$scope['all'+t])
    $scope[t+'s'].forEach(function(st){
      $scope.types[st].val=$scope['all'+t];
    });
    $scope.doNodeList();
  }
});