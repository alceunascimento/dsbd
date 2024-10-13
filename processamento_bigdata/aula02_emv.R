# X-bin (n, theta)
# theta ~ Beta (a, b)
# theta|x ~ beta (a+x, B+n)

n <- 10
x <- 2

a <- 1
b <- 1
theta <- seq(0,1, length.out = 1000)

plot(theta, dbeta(theta, a,b), type = "l", ylim = c(0,5))
lines(theta, dbeta(theta, a+x, b+n-x), col="red3")

emv <- x/n
emv
map <- (a+x-1)/(a+b+n-2)
map