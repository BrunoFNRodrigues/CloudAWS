output "password" {
  value = { for user, profile in aws_iam_user_login_profile.user_profile : user => profile.password }
}