import Base: -, +

abstract type Angle end

struct Radian <: Angle
  radians::Float64
end

# Degre, Minutes, Second (DMS)

struct DMS <: Angle
  seconds::Int
end

function Second(seconds::Integer)
  DMS(seconds)
end

function Minute(minutes::Integer)
  DMS(minutes * 60)
end


Degree(degrees::Integer) = Minute(degrees * 60)
Degree(deg::Integer, min::Integer) = Degree(deg) + Minute(min)

# Base add minus overloading

+(θ::DMS, α::DMS) = DMS(θ.seconds + α.seconds)
-(θ::DMS, α::DMS) = DMS(θ.seconds - α.seconds)

+(θ::Radian, α::Radian) = Radian(θ.radians + α.radians)
-(θ::Radian, α::Radian) = Radian(θ.radians - α.radians)
