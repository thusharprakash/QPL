var app = angular.module('qpl',['ngDialog']);

app.controller('qplController', ['$scope', 'ngDialog', '$compile', function($scope,ngDialog,$compile) {
	$scope.openTeam = function(teamName){
		ngDialog.open({
			template: 'teams/'+teamName,
			controller: 'firstDialogCtrl',
			closeByDocument: false,
            className: 'ngdialog-theme-default',
            closeByEscape: true,
            showClose: true,
            scope: $scope

		});
	};
	window.onload = function(){
		$compile(document.getElementsByTagName('body')[0])($scope);
	};
}]);

app.controller('firstDialogCtrl', ['$scope', 'ngDialog', function($scope, ngDialog){
	$scope.openPlayer = function(playerName){
		ngDialog.open({
			template: 'player/'+playerName+'/details',
			closeByDocument: true,
            className: 'ngdialog-theme-default',
            closeByEscape: true,
            showClose: true,
            scope: $scope
		});
	};
	
}]);