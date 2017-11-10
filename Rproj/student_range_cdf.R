# Display the Student's range distributions with various
# degrees of freedom.

svg(filename='StudentizedRangeCDF.svg')

x <- seq(0, 5, length=400)
hx <- pnorm(x)

k <- c(2, 2, 2, 3, 10)
df <- c(2, 4, 8, 10, 10)
colors <- c("red", "blue", "grey", "gold", "green", "black")
labels <- c("k=2 df=2", "k=2 df=4", "k=2 df=8", "k=3 df=10", "k=10 df=10", 
            "k=10 df=100")

# standard normal CDF
plot(x, ptukey(q=x, nmeans=10, df=100), lwd=2, col="black", 
     type="l", xlab="x", ylab="CDF F(x)", ylim=c(0, 1))

# studentized range distri.
for (i in 1:5){
  lines(x, ptukey(q=x, nmeans=k[i], df=df[i]), lwd=2, col=colors[i])
}

legend("topleft", inset=.05,
  labels, lwd=2, lty=c(1, 1, 1, 1, 1, 1), col=colors)


