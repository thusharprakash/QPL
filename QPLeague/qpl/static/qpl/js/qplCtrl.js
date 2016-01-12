var app = angular.module('qpl',['ngDialog']);

app.controller('qplController', function($scope,ngDialog,$compile) {
	$scope.openTeam = function(teamName){
		console.log(teamName);
		ngDialog.open({
			template: 'teams/'+teamName,
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
});