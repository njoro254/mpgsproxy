from flask import Blueprint

from prints.pagesMembers.api import MembersHomePageAPI, NotificationsPageAPI, ReportsPageAPI, DownloadsPageAPI

pagesMembers_app = Blueprint("pagesMembers_app", __name__)

memberspage_view = MembersHomePageAPI.as_view('memberspage_api')
# MEMBERS HOME PAGE PAGE URL
pagesMembers_app.add_url_rule('/index', 
	view_func=memberspage_view, 
	methods=['POST', 'GET'])


notifications_view = NotificationsPageAPI.as_view('notifications_api')
# NOTIFICATIONS PAGE URL
pagesMembers_app.add_url_rule('/notifications', 
	view_func=notifications_view, 
	methods=['POST', 'GET'])


# REPORTS PAGE URL
reports_view = ReportsPageAPI.as_view('reports_api')

pagesMembers_app.add_url_rule('/reports', 
	view_func=reports_view, 
	methods=['POST', 'GET'])


# DOWNLOADS PAGE URL
downloads_view = DownloadsPageAPI.as_view('downloads_api')

pagesMembers_app.add_url_rule('/downloads', 
	view_func=downloads_view, 
	methods=['POST', 'GET'])