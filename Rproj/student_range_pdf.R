# Display the Student's range distributions with various
# degrees of freedom.

svg(filename='StudentizedRangePDF.svg')

x <- seq(0, 5, length=400)
hx <- pnorm(x)

k <- c(2, 2, 2, 3, 10)
df <- c(2, 4, 8, 10, 10)
colors <- c("red", "blue", "grey", "gold", "green", "black")
labels <- c("k=2 df=2", "k=2 df=4", "k=2 df=8", "k=3 df=10", "k=10 df=10", 
            "k=10 df=100")

dtukey <- function(q, nmeans, df) {
    delta = 0.001
    return (ptukey(q+delta, nmeans, df) - ptukey(q, nmeans, df)) / delta
}

# standard normal PDF
plot(x, dtukey(q=x, nmeans=10, df=100), lwd=2, col="black", 
     type="l", xlab="x", ylab="PDF f(x)", ylim=c(0, 6e-4))

# studentized range distri.
for (i in 1:5){
  lines(x, dtukey(q=x, nmeans=k[i], df=df[i]), lwd=2, col=colors[i])
}

legend("topright", inset=.05,
  labels, lwd=2, lty=c(1, 1, 1, 1, 1, 1), col=colors)


