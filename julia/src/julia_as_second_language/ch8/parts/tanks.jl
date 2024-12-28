import Base: isempty

export SmallTank, MediumTank, LargeTank
export Tank, drymass, totalmass, propellant, propellant!
export refill!, consume!
export mass

abstract type Tank end

mutable struct SmallTank <: Tank
  propellant::Float64
end

mutable struct MediumTank <: Tank
  propellant::Float64
end

mutable struct LargeTank <: Tank
  propellant::Float64
end

# --- Mass ---
drymass(::Type{SmallTank}) = 40.0
drymass(::Type{MediumTank}) = 250.0
drymass(::Type{LargeTank}) = 950.0

totalmass(::Type{SmallTank}) = 410.0
totalmass(::Type{MediumTank}) = 2300.0
totalmass(::Type{LargeTank}) = 10200.0

# --- propellant function ---

propellant(tank::Tank) = tank.propellant

function propellant!(tank::Tank, amount::Real)
  tank.propellant = amount
end

isempty(tank::Tank) = tank.propellant <= 0

mass(tank::Tank) = drymass(tank) + propellant(tank)

function refill!(tank::Tank)
  propellant!(tank, totalmass(tank) - drymass(tank))
  tank
end

function consume!(tank::Tank, amount::Real)
  remaining = max(propellant(tank) - amount, 0)
  propellant!(tank, remaining)
  remaining
end

