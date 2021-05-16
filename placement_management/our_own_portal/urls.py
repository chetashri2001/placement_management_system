from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("loginform", views.loginform, name="loginform"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("studentform", views.studentform, name="studentform"),
    path("companyform", views.companyform, name="companyform"),
    path("addjobform", views.addjobform, name="addjobform"),
    path("do_login", views.do_login, name="do_login"),
    path("do_student_register", views.do_student_register, name="do_student_register"),
    path("do_company_register", views.do_company_register, name="do_company_register"),
    path("admin_base_page", views.admin_base_page, name="admin_base_page"),
    path("company_base_page", views.company_base_page, name="company_base_page"),
    path("student_base_page", views.student_base_page, name="student_base_page"),
    path("do_add_job", views.do_add_job, name="do_add_job"),
    path("view_job", views.view_job, name="view_job"),
    path("view_job_for_student", views.view_job_for_student, name="view_job_for_student"),
    path("view_job_for_company", views.view_job_for_company, name="view_job_for_company"),
    path("view_all_student", views.view_all_student, name="view_all_student"),
    path("view_all_company", views.view_all_company, name="view_all_company"),
    path("applied_for_student", views.applied_for_student, name="applied_for_student"),
    path("applied_for_company", views.applied_for_company, name="applied_for_company"),
    path("applied_for_admin", views.applied_for_admin, name="applied_for_admin"),
    path("selected_for_company", views.selected_for_company, name="selected_for_company"),
    path("selected_for_student", views.selected_for_student, name="selected_for_student"),
    path("selected_for_admin", views.selected_for_admin, name="selected_for_admin"),
    path("company_profile", views.company_profile, name="company_profile"),
    path("student_profile", views.student_profile, name="student_profile"),
    path("edit_student_profile", views.edit_student_profile, name="edit_student_profile"),
    path("edit_company_profile", views.edit_company_profile, name="edit_company_profile"),
    path("/student_profile_for_company/<str:id>", views.student_profile_for_company, name="student_profile_for_company"),
    path("/edit_job/<str:id>", views.edit_job, name="edit_job"),
    path("save_student_profile", views.save_student_profile, name="save_student_profile"),
    path("save_company_profile", views.save_company_profile, name="save_company_profile"),
    path("save_edit_job", views.save_edit_job, name="save_edit_job"),
    path("/apply_for_job/<str:id>", views.apply_for_job, name="apply_for_job"),
    path("save_applied_job", views.save_applied_job, name="save_applied_job"),
    path("/select_student/<str:id>", views.select_student, name="select_student"),
    path("/reject_student/<str:id>", views.reject_student, name="reject_student"),
    path("/delete_company/<str:id>", views.delete_company, name="delete_company"),
    path("/delete_student/<str:id>", views.delete_student, name="delete_student"),
    path("data_count", views.data_count, name="data_count"),
    path("invalid_login", views.invalid_login, name="invalid_login")

]

